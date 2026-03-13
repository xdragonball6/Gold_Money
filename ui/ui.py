from datetime import datetime
from data.fetcher import fetch_fx_rates, fetch_gold_krw, resolve_ticker, fetch_stock

from PySide6.QtCore import Qt, QThread, Signal, QTimer
from PySide6.QtWidgets import QMainWindow, QLabel, QFrame

from .qt import Ui_MainWindow


# ── 마켓 설정 (탭 추가/삭제 시 여기만 수정) ───────────────────────────────────
# { 한글 마켓명: uic 위젯 suffix }
# uic 위젯 이름 규칙: search_input_{suffix}, search_btn_{suffix}, result_layout_{suffix}
MARKETS = {
    "한국": "korea",
    "일본": "japan",
    "미국": "us",
    "유럽": "europe",
}

# { 환율 코드: uic 위젯 suffix }
# uic 위젯 이름 규칙: fx_label_{suffix}
FX_CODES = {
    "USD": "usd",
    "JPY": "jpy",
    "EUR": "eur",
    "CNY": "cny",
}


# ── 백그라운드 워커 ────────────────────────────────────────────────────────────

class FxGoldWorker(QThread):
    finished = Signal(dict, dict)
    error = Signal(str)

    def run(self):
        try:
            fx = fetch_fx_rates()
            gold = fetch_gold_krw(usd_krw_rate=fx.get("USD", {}).get("rate"))
            self.finished.emit(fx, gold)
        except Exception as e:
            self.error.emit(str(e))


class StockWorker(QThread):
    finished = Signal(dict)
    error = Signal(str)

    def __init__(self, raw_ticker: str, market: str, parent=None):
        super().__init__(parent)
        self.raw_ticker = raw_ticker
        self.market = market

    def run(self):
        try:
            ticker = resolve_ticker(self.raw_ticker, self.market)
            if ticker is None:
                self.error.emit("종목 코드가 비어 있습니다.")
                return
            self.finished.emit(fetch_stock(ticker))
        except Exception as e:
            self.error.emit(str(e))


# ── 메인 윈도우 ────────────────────────────────────────────────────────────────

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self._fx_worker = None
        self._stock_workers: dict[str, StockWorker] = {}

        for market in MARKETS:
            self.search_btn(market).clicked.connect(
                lambda _=False, m=market: self._on_search(m)
            )
            self.search_input(market).returnPressed.connect(
                lambda m=market: self._on_search(m)
            )

        self._refresh_timer = QTimer(self)
        self._refresh_timer.timeout.connect(self.refresh_fx_gold)
        self._refresh_timer.start(60_000)
        self.refresh_fx_gold()

    # ── uic 위젯 접근 헬퍼 (이름 규칙 한 곳에서 관리) ────────────────────────

    def search_input(self, market: str):
        return getattr(self, f"search_input_{MARKETS[market]}")

    def search_btn(self, market: str):
        return getattr(self, f"search_btn_{MARKETS[market]}")

    def result_layout(self, market: str):
        return getattr(self, f"result_layout_{MARKETS[market]}")

    def fx_label(self, code: str):
        return getattr(self, f"fx_label_{FX_CODES[code]}")

    # ── 환율 / 금 시세 ────────────────────────────────────────────────────────

    def refresh_fx_gold(self):
        if self._fx_worker and self._fx_worker.isRunning():
            return
        self.gold_label.setText("순금  업데이트 중...")
        self._fx_worker = FxGoldWorker()
        self._fx_worker.finished.connect(self.on_fx_gold_ready)
        self._fx_worker.error.connect(self.on_fx_gold_error)
        self._fx_worker.start()

    def on_fx_gold_ready(self, fx: dict, gold: dict):
        price_krw = gold.get("price_krw")
        pct = gold.get("change_pct")
        if price_krw is not None:
            pct_str = f"  {_pct_str(pct)}" if pct is not None else ""
            self.gold_label.setText(f"순금  ₩{price_krw * 3.75:,.0f}/3.75g{pct_str}")
        else:
            self.gold_label.setText("순금  데이터 없음")

        for code in FX_CODES:
            rate = fx.get(code, {}).get("rate")
            cpct = fx.get(code, {}).get("change_pct")
            lbl = self.fx_label(code)
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

    def on_fx_gold_error(self, msg: str):
        self.gold_label.setText("순금  연결 오류")
        self.update_time_label.setText("업데이트 실패")

    # ── 주식 검색 ─────────────────────────────────────────────────────────────

    def _on_search(self, market: str):
        raw = self.search_input(market).text().strip()
        if not raw:
            return

        self.search_btn(market).setEnabled(False)
        self.search_btn(market).setText("...")
        self._set_result_loading(market)

        old = self._stock_workers.get(market)
        if old and old.isRunning():
            old.quit()

        worker = StockWorker(raw, market)
        worker.finished.connect(lambda data, m=market: self._on_stock_ready(m, data))
        worker.error.connect(lambda err, m=market: self._on_stock_error(m, err))
        worker.finished.connect(lambda _, m=market: self._restore_btn(m))
        worker.error.connect(lambda _, m=market: self._restore_btn(m))
        self._stock_workers[market] = worker
        worker.start()

    def _restore_btn(self, market: str):
        self.search_btn(market).setEnabled(True)
        self.search_btn(market).setText("검색")

    def _on_stock_ready(self, market: str, data: dict):
        layout = self.result_layout(market)
        self._clear_layout(layout)

        if data.get("error"):
            err = QLabel(f"오류: {data['error']}")
            err.setObjectName("error_label")
            err.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(err)
            return

        name_lbl = QLabel(data.get("name", data["ticker"]))
        name_lbl.setObjectName("res_name")
        ticker_lbl = QLabel(data["ticker"])
        ticker_lbl.setObjectName("res_ticker")

        price = data["price"]
        currency_sym = _currency_symbol(data.get("currency", ""))
        price_lbl = QLabel(f"{currency_sym}{price:,.2f}" if price else "--")
        price_lbl.setObjectName("res_price")

        pct = data.get("change_pct")
        chg_abs = data.get("change_abs")
        if pct is not None:
            arrow = "▲" if pct >= 0 else "▼"
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
        layout = self.result_layout(market)
        self._clear_layout(layout)
        err_lbl = QLabel(f"오류: {err}")
        err_lbl.setObjectName("error_label")
        err_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(err_lbl)

    def _set_result_loading(self, market: str):
        layout = self.result_layout(market)
        self._clear_layout(layout)
        loading = QLabel("데이터 로딩 중...")
        loading.setObjectName("loading_label")
        loading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(loading)

    @staticmethod
    def _clear_layout(layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()


# ── 유틸 ──────────────────────────────────────────────────────────────────────

def _pct_str(pct):
    if pct is None:
        return ""
    return f"{'+'if pct >= 0 else ''}{pct:.2f}%"

def _pct_color_style(pct):
    if pct is None:
        return "color: #a0aabb;"
    if pct > 0:
        return "color: #3ddc84; font-size: 12px;"
    if pct < 0:
        return "color: #ff5f5f; font-size: 12px;"
    return "color: #a0aabb; font-size: 12px;"

def _currency_symbol(currency):
    return {
        "KRW": "₩", "USD": "$", "JPY": "¥",
        "EUR": "€", "GBP": "£", "CNY": "¥",
        "HKD": "HK$", "SGD": "S$",
    }.get(currency.upper() if currency else "", "")