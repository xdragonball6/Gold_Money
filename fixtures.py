"""
fixtures.py — Gold Money 프로젝트 테스트 픽스처
===============================================
autotest.py 와 같은 폴더에 위치시키세요.
autotest.py 는 절대 수정하지 않습니다.
이 파일만 프로젝트마다 1회 작성합니다.
"""

import sys, importlib.util, queue
from unittest.mock import MagicMock, patch

# ----------------------------------------------------------------
# MOCK_MODULES: 설치되지 않아 Mock 처리할 패키지 목록
# ----------------------------------------------------------------
MOCK_MODULES = [
    "PySide6", "PySide6.QtCore", "PySide6.QtWidgets", "PySide6.QtGui",
    "yfinance", "psutil", "pandas", "data", "data.fetcher",
]

# ----------------------------------------------------------------
# FIXTURE_VARS: body에 이 변수가 있으면 _make_logic() 자동 주입
# CONFIG_VARS : body에 이 변수가 있으면 _load_config() 자동 주입
# ----------------------------------------------------------------
FIXTURE_VARS = ["logic", "q_out"]
CONFIG_VARS  = ["cfg"]

# ----------------------------------------------------------------
# _FILE_MAP: autotest.py 가 런타임에 주입 (IDE 경고 방지용 선언)
# ----------------------------------------------------------------
_FILE_MAP: dict = {}


def _load_config():
    """
    config 모듈 로드.
    이미 로드된 경우 캐시를 반환한다.
    → _make_logic() 과 테스트 메서드가 동일한 SignalType 인스턴스를 공유하게 됨
    """
    if "config" in sys.modules:
        return sys.modules["config"]
    spec = importlib.util.spec_from_file_location("config", _FILE_MAP["config"])
    mod  = importlib.util.module_from_spec(spec)
    sys.modules["config"] = mod
    spec.loader.exec_module(mod)
    return mod


def _make_logic():
    """
    LogicProcess 인스턴스 생성
    - run() 블로킹 방지를 위해 patch 적용
    - queue.Queue 사용 (multiprocessing.Queue 는 Enum pickle 오류 발생)
    """
    cfg  = _load_config()
    spec = importlib.util.spec_from_file_location("lp_mod", _FILE_MAP["LogicProcess"])
    lp   = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lp)

    q_in  = queue.Queue()
    q_out = queue.Queue()

    with patch.object(lp.LogicProcess, "run",   return_value=None), \
         patch.object(lp.PIDChecker,   "start", return_value=None):
        inst = lp.LogicProcess(q_in=q_in, q_out=q_out)

    return inst, q_out, cfg.SignalType