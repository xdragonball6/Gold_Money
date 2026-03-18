import os
import sys
import time
import queue
import signal
import psutil
from threading import Thread
from multiprocessing import Queue
from config import SignalType


# ── PID 감시 스레드 ────────────────────────────────────────────────────────────

class PIDChecker(Thread):
    """부모 프로세스(UI)가 살아 있는지 주기적으로 감시."""

    def __init__(self, logic_thread):
        super().__init__()
        self.logic_thread: LogicProcess = logic_thread
        self.daemon = True

    def run(self):
        print("PIDChecker start ...")
        while self.logic_thread.running_flag:
            try:
                if not self.logic_thread.check_parent_pid():
                    break
                time.sleep(10)
            except Exception as e:
                print(e)
        print("PIDChecker end ...")


# ── 메인 로직 프로세스 ─────────────────────────────────────────────────────────

class LogicProcess:
    """
    UI 큐(q_in)에서 신호를 수신하고, 처리 결과를 결과 큐(q_out)로 전송.

    신호 흐름
    ---------
    UI ──[UI_QUEUE]──► process_data()
         FETCH_FX_GOLD  →  _handle_fetch_fx_gold()  →  [LOGIC_QUEUE] ──► UI
         FETCH_STOCK    →  _handle_fetch_stock()     →  [LOGIC_QUEUE] ──► UI
         EXIT_PROGRAM   →  sys.exit()
         LOGIN          →  (인증 후) _send(LOGIN, ...)

    데이터 조회는 별도 데몬 스레드에서 수행하므로
    큐 소비 루프가 블로킹되지 않는다.
    """

    def __init__(self, q_in: Queue = None, q_out: Queue = None):
        self.q_in  = q_in
        self.q_out = q_out
        self.running_flag = True
        self.parent_pid   = os.getppid()

        pid_checker = PIDChecker(self)
        pid_checker.start()

        self.run()

    # ── 전송 헬퍼 ─────────────────────────────────────────────────────────────

    def _send(self, signal_type: SignalType, data: dict):
        """UI 프로세스에 결과 전송."""
        self.q_out.put(dict(type=signal_type, data=data))

    # ── 신호별 핸들러 ──────────────────────────────────────────────────────────

    def _handle_fetch_fx_gold(self, _data: dict):
        """
        환율·금 시세 조회 요청 처리.
        네트워크 I/O 는 데몬 스레드에서 수행한다.
        완료 시 FX_GOLD_RESULT 또는 FX_GOLD_ERROR 를 UI로 전송.
        """
        def _fetch():
            try:
                from data.fetcher import fetch_fx_rates, fetch_gold_krw
                fx   = fetch_fx_rates()
                gold = fetch_gold_krw(usd_krw_rate=fx.get("USD", {}).get("rate"))
                self._send(SignalType.FX_GOLD_RESULT, dict(fx=fx, gold=gold))
            except Exception as e:
                self._send(SignalType.FX_GOLD_ERROR, dict(message=str(e)))

        Thread(target=_fetch, daemon=True).start()

    def _handle_fetch_stock(self, data: dict):
        """
        주식 시세 조회 요청 처리.
        네트워크 I/O 는 데몬 스레드에서 수행한다.
        완료 시 STOCK_RESULT 또는 STOCK_ERROR 를 UI로 전송.

        data 필드
        ---------
        raw    : 사용자 입력 종목 코드
        market : 마켓 이름 (한국/일본/미국/유럽)
        """
        def _fetch():
            market = data.get("market", "")
            try:
                from data.fetcher import resolve_ticker, fetch_stock
                raw    = data.get("raw", "")
                ticker = resolve_ticker(raw, market)
                if ticker is None:
                    self._send(
                        SignalType.STOCK_ERROR,
                        dict(market=market, message="종목 코드가 비어 있습니다."),
                    )
                    return
                result = fetch_stock(ticker)
                self._send(SignalType.STOCK_RESULT, dict(market=market, data=result))
            except Exception as e:
                self._send(SignalType.STOCK_ERROR, dict(market=market, message=str(e)))

        Thread(target=_fetch, daemon=True).start()

    def _handle_login(self, data: dict):
        """
        로그인 처리.

        data 필드
        ---------
        id : 사용자 ID
        pw : 비밀번호

        TODO: 실제 인증 서버 연동으로 교체
        응답: SignalType.LOGIN  { success: bool, message: str (실패 시) }
        """
        user_id  = data.get("id", "")
        password = data.get("pw", "")

        # --- 인증 로직 구현 위치 ---
        # 현재는 비어 있지 않으면 성공으로 처리
        if user_id and password:
            self._send(SignalType.LOGIN, dict(success=True))
        else:
            self._send(SignalType.LOGIN, dict(success=False, message="ID 또는 비밀번호가 올바르지 않습니다."))

    # ── 신호 디스패처 ──────────────────────────────────────────────────────────

    def process_data(self, queue_data_dict: dict):
        """
        큐에서 꺼낸 패킷을 SignalType 에 따라 적절한 핸들러로 위임.

        패킷 형식: { 'type': SignalType, 'data': dict }
        """
        try:
            data        = queue_data_dict.get("data", {})
            signal_type = queue_data_dict.get("type")

            if signal_type == SignalType.EXIT_PROGRAM:
                self.running_flag = False
                sys.exit(0)

            elif signal_type == SignalType.LOGIN:
                self._handle_login(data)

            elif signal_type == SignalType.FETCH_FX_GOLD:
                self._handle_fetch_fx_gold(data)

            elif signal_type == SignalType.FETCH_STOCK:
                self._handle_fetch_stock(data)

            else:
                print(f"[LogicProcess] 알 수 없는 신호: {signal_type}")

        except Exception as e:
            print(f"[LogicProcess] process_data 오류: {e}")

    # ── 큐 소비 루프 ───────────────────────────────────────────────────────────

    def consume_que(self, exit_time: float = 1.0):
        """
        exit_time 초 동안 q_in 을 폴링한다.
        데이터가 없으면 조용히 반환.
        """
        start = time.time()
        while True:
            time.sleep(0.05)
            if time.time() - start > exit_time:
                return
            try:
                data = self.q_in.get(timeout=0.5)
                self.process_data(data)
            except queue.Empty:
                continue

    def run(self):
        print("LogicProcess start ...")
        while self.running_flag:
            self.consume_que(5)
        print("logic end ...")
        os.kill(os.getpid(), signal.SIGTERM)

    # ── 부모 PID 감시 ─────────────────────────────────────────────────────────

    def check_parent_pid(self) -> bool:
        try:
            if psutil.pid_exists(self.parent_pid):
                return True
        except Exception as e:
            print(f"[PIDChecker] 오류: {e}")
        print("parent pid not found .. exit program")
        self.running_flag = False
        return False