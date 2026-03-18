"""
ui.py - MainWindow

역할
----
* 사용자 입력(버튼 클릭, 타이머)을 Signal 로 변환 → signal_logic() 으로 Logic 프로세스에 전달
* ObserverThread 가 Logic 큐에서 수신한 결과를 process() 에서 받아 UI 위젯 업데이트

UI 는 데이터 조회 로직을 직접 실행하지 않는다.
모든 비즈니스 로직은 LogicProcess 에서 처리된다.
"""

from datetime import datetime

from PySide6.QtCore import Qt, QThread, Signal, QTimer
from PySide6.QtWidgets import QMainWindow, QLabel, QFrame

from .qt import *
import config as cf
from config import SignalType
import time


# ── Logic 큐 감시 스레드 ───────────────────────────────────────────────────────

class ObserverThread(QThread):
    """
    별도 스레드에서 LOGIC_QUEUE 를 blocking wait 하다가
    데이터가 도착하면 Qt 시그널로 메인 스레드에 전달.
    """
    logic_signal = Signal(object)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logic_queue = cf.LOGIC_QUEUE

    def run(self):
        while True:
            data = self.logic_queue.get()   # blocking
            self.logic_signal.emit(data)


# ── 마켓 / 환율 매핑 ─────────────────────────────────────────────────────────

MARKETS = {
    "한국": "korea",
    "일본": "japan",
    "미국": "us",
    "유럽": "europe",
}

FX_CODES = {
    "USD": "usd",
    "JPY": "jpy",
    "EUR": "eur",
    "CNY": "cny",
}


# ── 메인 윈도우 ────────────────────────────────────────────────────────────────

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, logic_process, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.logic_process = logic_process
        self.ui_queue      = cf.UI_QUEUE

        # Logic 큐 감시 스레드 시작
        self.observer_thread = ObserverThread(self)
        self.observer_thread.logic_signal.connect(self.process)
        self.observer_thread.start()

        # 로딩 오버레이 / 로그인 다이얼로그
        self.loading      = LoadingWidget(self.main_widget)
        self.login_dialog = LoginDialog()
        self.login_dialog.exit_btn.clicked.connect(lambda: self.close(True))
        self.login_dialog.login_btn.clicked.connect(self.clicked_login)

        # 마켓별 검색 버튼 · 엔터키 연결
        for market in MARKETS:
            self.search_btn(market).clicked.connect(
                lambda _=False, m=market: self._on_search(m)
            )
            self.search_input(market).returnPressed.connect(
                lambda m=market: self._on_search(m)
            )

        # 60 초마다 환율·금 시세 자동 갱신
        self._refresh_timer = QTimer(self)
        self._refresh_timer.timeout.connect(self.refresh_fx_gold)
        self._refresh_timer.start(60_000)
        self.refresh_fx_gold()

        self.login_dialog.show()

    def closeEvent(self, event):
        print('close event')
        self.close()
        event.ignore()

    def close(self, is_force=False):
        time.sleep(0.1)
        if is_force:
            self.signal_logic(SignalType.EXIT_PROGRAM, {})
            print("Closing Force....")
            sys.exit(0)

        from PySide6.QtWidgets import QMessageBox
        reply = QMessageBox.question(
            self, "종료", "프로그램을 종료하시겠습니까?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.signal_logic(SignalType.EXIT_PROGRAM, {})
            print("Closing....")
            sys.exit(0)

    # =========================================================================
    # Logic ↔ UI 통신
    # =========================================================================

    # =========================================================================
    # 로그인 버튼 클릭 핸들러
    # =========================================================================

    def clicked_login(self):
        """
        로그인 버튼 클릭 시 호출.
        ID / PW 를 읽어 Logic 프로세스에 LOGIN 신호를 전송.
        응답은 process() -> _on_login_result() 에서 처리.
        """
        user_id  = self.login_dialog.id_edit.text().strip()
        password = self.login_dialog.pw_edit.text().strip()

        if not user_id or not password:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self.login_dialog, "입력 오류", "ID와 비밀번호를 입력해주세요.")
            return

        # 로그인 중 버튼 비활성화 + 로딩 표시
        self.login_dialog.login_btn.setEnabled(False)
        self.login_dialog.login_btn.setText("로그인 중...")
        self.login_dialog.loading.start()

        self.signal_logic(SignalType.LOGIN, dict(id=user_id, pw=password))

    def signal_logic(self, signal_type: SignalType, data: dict,
                     wait_loading: bool = False):
        """
        Logic 프로세스에 신호(패킷)를 전송한다.

        패킷 형식: { 'type': SignalType, 'data': dict }
        wait_loading=True 이면 로딩 오버레이를 표시한다.
        """
        self.ui_queue.put(dict(type=signal_type, data=data))
        if wait_loading:
            self.loading.start()

    def process(self, signal: dict):
        """
        Logic 프로세스로부터 수신된 신호를 SignalType 에 따라
        해당 UI 업데이트 메서드로 위임.

        패킷 형식: { 'type': SignalType, 'data': dict }
        """
        signal_type = signal.get("type")
        data        = signal.get("data", {})

        if signal_type == SignalType.LOGIN:
            self._on_login_result(data)

        elif signal_type == SignalType.FX_GOLD_RESULT:
            self._on_fx_gold_ready(data.get("fx", {}), data.get("gold", {}))

        elif signal_type == SignalType.FX_GOLD_ERROR:
            self._on_fx_gold_error(data.get("message", "알 수 없는 오류"))

        elif signal_type == SignalType.STOCK_RESULT:
            self._on_stock_ready(data.get("market", ""), data.get("data", {}))

        elif signal_type == SignalType.STOCK_ERROR:
            self._on_stock_error(data.get("market", ""), data.get("message", "알 수 없는 오류"))

    # =========================================================================
    # 로그인
    # =========================================================================

    def _on_login_result(self, data: dict):
        """Logic 에서 로그인 결과 수신 → 성공 시 메인 화면 전환 / 실패 시 오류 표시."""
        # 버튼 · 로딩 상태 항상 복구
        self.login_dialog.login_btn.setEnabled(True)
        self.login_dialog.login_btn.setText(" 로그인")
        self.login_dialog.loading.end()

        if data.get("success"):
            print("로그인 성공 - 메인 화면으로 이동")
            self.login_dialog.hide()
            self.show()
        else:
            from PySide6.QtWidgets import QMessageBox
            msg = data.get("message", "로그인에 실패했습니다.")
            QMessageBox.warning(self.login_dialog, "로그인 실패", msg)

    # =========================================================================
    # 위젯 접근 헬퍼 (이름 규칙을 한 곳에서 관리)
    # =========================================================================

    def search_input(self, market: str):
        return getattr(self, f"search_input_{MARKETS[market]}")

    def search_btn(self, market: str):
        return getattr(self, f"search_btn_{MARKETS[market]}")

    def result_layout(self, market: str):
        return getattr(self, f"result_layout_{MARKETS[market]}")

    def fx_label(self, code: str):
        return getattr(self, f"fx_label_{FX_CODES[code]}")

    # =========================================================================
    # 환율 / 금 시세
    # =========================================================================

    def refresh_fx_gold(self):
        """환율·금 시세 조회 요청 → Logic 프로세스."""
        self.gold_label.setText("순금  업데이트 중...")
        self.signal_logic(SignalType.FETCH_FX_GOLD, {})

    def _on_fx_gold_ready(self, fx: dict, gold: dict):
        """FX_GOLD_RESULT 수신 → 티커바 레이블 갱신."""
        price_krw = gold.get("price_krw")
        pct       = gold.get("change_pct")
        if price_krw is not None:
            pct_str = f"  {_pct_str(pct)}" if pct is not None else ""
            self.gold_label.setText(f"순금  ₩{price_krw * 3.75:,.0f}/3.75g{pct_str}")
        else:
            self.gold_label.setText("순금  데이터 없음")

        for code in FX_CODES:
            rate = fx.get(code, {}).get("rate")
            cpct = fx.get(code, {}).get("change_pct")
            lbl  = self.fx_label(code)
            if rate is not None:
                pct_str = f" ({_pct_str(cpct)})" if cpct is not None else ""
                if code == "JPY":
                    lbl.setText(f"₩{rate:.2f}{pct_str}")
                elif code == "CNY":
                    lbl.setText(f"₩{rate:.1f}{pct_str}")
                else:
                    lbl.setText(f"₩{rate:,.1f}{pct_str}")
                lbl.setStyleSheet(_pct_color_style(cpct))
            else:
                lbl.setText("--")

        self.update_time_label.setText(datetime.now().strftime("%H:%M 기준"))

    def _on_fx_gold_error(self, msg: str):
        """FX_GOLD_ERROR 수신 → 오류 표시."""
        self.gold_label.setText("순금  연결 오류")
        self.update_time_label.setText("업데이트 실패")

    # =========================================================================
    # 주식 검색
    # =========================================================================

    def _on_search(self, market: str):
        """
        검색 버튼 클릭 / 엔터키 → FETCH_STOCK 신호를 Logic 에 전송.
        UI 는 버튼 비활성화와 로딩 텍스트 표시만 담당.
        """
        raw = self.search_input(market).text().strip()
        if not raw:
            return

        # 버튼 비활성화 · 로딩 표시
        self.search_btn(market).setEnabled(False)
        self.search_btn(market).setText("...")
        self._set_result_loading(market)

        # Logic 프로세스에 조회 요청
        self.signal_logic(SignalType.FETCH_STOCK, dict(raw=raw, market=market))

    def _on_stock_ready(self, market: str, data: dict):
        """STOCK_RESULT 수신 → 결과 카드 갱신."""
        self._restore_btn(market)
        layout = self.result_layout(market)
        self._clear_layout(layout)

        if data.get("error"):
            err = QLabel(f"오류: {data['error']}")
            err.setObjectName("error_label")
            err.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(err)
            return

        name_lbl   = QLabel(data.get("name", data["ticker"]))
        name_lbl.setObjectName("res_name")
        ticker_lbl = QLabel(data["ticker"])
        ticker_lbl.setObjectName("res_ticker")

        price        = data["price"]
        currency_sym = _currency_symbol(data.get("currency", ""))
        price_lbl    = QLabel(f"{currency_sym}{price:,.2f}" if price else "--")
        price_lbl.setObjectName("res_price")

        pct     = data.get("change_pct")
        chg_abs = data.get("change_abs")
        if pct is not None:
            arrow   = "▲" if pct >= 0 else "▼"
            abs_str = f"{currency_sym}{abs(chg_abs):,.2f}  " if chg_abs is not None else ""
            chg_lbl = QLabel(f"{arrow}  {abs_str}{_pct_str(pct)}")
            chg_lbl.setObjectName(
                "res_change_pos" if pct > 0 else
                "res_change_neg" if pct < 0 else
                "res_change_neu"
            )
        else:
            chg_lbl = QLabel("전일 데이터 없음")
            chg_lbl.setObjectName("res_change_neu")

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("color: #2a3040;")

        for w in (name_lbl, ticker_lbl, line, price_lbl, chg_lbl):
            layout.addWidget(w)

        ts = QLabel(datetime.now().strftime("조회 시각: %Y-%m-%d %H:%M:%S"))
        ts.setObjectName("status_label")
        layout.addWidget(ts)

    def _on_stock_error(self, market: str, err: str):
        """STOCK_ERROR 수신 → 오류 메시지 표시."""
        self._restore_btn(market)
        layout = self.result_layout(market)
        self._clear_layout(layout)
        err_lbl = QLabel(f"오류: {err}")
        err_lbl.setObjectName("error_label")
        err_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(err_lbl)

    # ── 버튼 상태 ─────────────────────────────────────────────────────────────

    def _restore_btn(self, market: str):
        self.search_btn(market).setEnabled(True)
        self.search_btn(market).setText("검색")

    def _set_result_loading(self, market: str):
        layout = self.result_layout(market)
        self._clear_layout(layout)
        loading = QLabel("데이터 로딩 중...")
        loading.setObjectName("loading_label")
        loading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(loading)

    # ── 레이아웃 유틸 ─────────────────────────────────────────────────────────

    @staticmethod
    def _clear_layout(layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()


# ── 표시 유틸 ─────────────────────────────────────────────────────────────────

def _pct_str(pct) -> str:
    if pct is None:
        return ""
    return f"{'+'if pct >= 0 else ''}{pct:.2f}%"


def _pct_color_style(pct) -> str:
    if pct is None:
        return "color: #a0aabb;"
    if pct > 0:
        return "color: #3ddc84; font-size: 12px;"
    if pct < 0:
        return "color: #ff5f5f; font-size: 12px;"
    return "color: #a0aabb; font-size: 12px;"


def _currency_symbol(currency: str) -> str:
    return {
        "KRW": "₩", "USD": "$", "JPY": "¥",
        "EUR": "€", "GBP": "£", "CNY": "¥",
        "HKD": "HK$", "SGD": "S$",
    }.get(currency.upper() if currency else "", "")