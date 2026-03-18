import os
import multiprocessing
from enum import Enum
from collections.abc import Mapping

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UI_QUEUE    = multiprocessing.Queue()   # UI → Logic  (요청)
LOGIC_QUEUE = multiprocessing.Queue()   # Logic → UI  (응답)


class DataClass(Mapping):
    def __call__(self, *args, **kwargs) -> dict:
        result = self.__dict__
        if args:
            result = {key: result.get(key) for key in args if result.get(key) is not None}
        if kwargs:
            result.update(kwargs)
        return result

    def __setitem__(self, key, value):
        self.__setattr__(str(key), value)

    def __getitem__(self, item):
        return self.__getattribute__(str(item))

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)


class SignalType(Enum):
    """
    UI <-> Logic 프로세스 간 통신에 사용되는 신호 타입.

    방향          | 신호
    ─────────────────────────────────────────────────────
    공통          | EXIT_PROGRAM, LOGIN
    UI -> Logic   | FETCH_FX_GOLD, FETCH_STOCK
    Logic -> UI   | FX_GOLD_RESULT, STOCK_RESULT,
                  | FX_GOLD_ERROR,  STOCK_ERROR
    """
    # 공통
    EXIT_PROGRAM   = -1   # 프로그램 종료
    LOGIN          = 0    # 로그인 요청 / 결과

    # UI -> Logic (요청)
    FETCH_FX_GOLD  = 1    # 환율·금 시세 조회 요청  data: {}
    FETCH_STOCK    = 2    # 주식 시세 조회 요청       data: {raw, market}

    # Logic -> UI (응답)
    FX_GOLD_RESULT = 3    # 환율·금 시세 결과        data: {fx, gold}
    STOCK_RESULT   = 4    # 주식 시세 결과            data: {market, data}
    FX_GOLD_ERROR  = 5    # 환율·금 조회 오류         data: {message}
    STOCK_ERROR    = 6    # 주식 조회 오류             data: {market, message}


# 하위 호환 상수
EXIT_PROGRAM = SignalType.EXIT_PROGRAM.value
LOGIN        = SignalType.LOGIN.value
