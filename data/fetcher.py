"""
fetcher.py – yfinance 기반 시세 데이터 조회 모듈
"""
import yfinance as yf

# ── 상수 ──────────────────────────────────────────────────────────────────────
TROY_OZ_TO_GRAM = 31.1035          # 트로이온스 → 그램 변환 계수

# 항상 표시할 환율 티커  (기준: 1 외화 = ? 원)
FX_TICKERS = {
    "USD": "USDKRW=X",
    "JPY": "JPYKRW=X",
    "EUR": "EURKRW=X",
    "CNY": "CNYKRW=X",
}

# 국가별 거래소 접미사 및 통화
MARKET_INFO = {
    "한국": {"suffixes": [".KS", ".KQ"], "currency": "KRW", "hint": "예) 005930  →  005930.KS"},
    "일본": {"suffixes": [".T"],          "currency": "JPY", "hint": "예) 7203  →  7203.T"},
    "미국": {"suffixes": [""],            "currency": "USD", "hint": "예) AAPL, TSLA, MSFT"},
    "유럽": {"suffixes": [".PA", ".DE", ".L", ".MI", ".AS", ".MC"],
              "currency": "EUR",
              "hint": "예) AIR.PA(파리) / VOW3.DE(독일) / SHEL.L(런던)"},
}


# ── 헬퍼 함수 ─────────────────────────────────────────────────────────────────

def _get_close_and_prev(ticker_str: str):
    """최근 2거래일의 종가를 반환. (오늘종가, 전일종가) – 실패 시 (None, None)"""
    try:
        tk = yf.Ticker(ticker_str)
        hist = tk.history(period="5d")
        if hist is None or len(hist) < 2:
            return None, None
        closes = hist["Close"].dropna()
        if len(closes) < 2:
            return None, None
        return float(closes.iloc[-1]), float(closes.iloc[-2])
    except Exception:
        return None, None


def _pct_change(today, prev):
    """전일 대비 변화율(%) 계산"""
    if today is None or prev is None or prev == 0:
        return None
    return (today - prev) / prev * 100.0


# ── 공개 API ──────────────────────────────────────────────────────────────────

def fetch_fx_rates() -> dict:
    """
    환율 딕셔너리 반환
    {
      "USD": {"rate": 1380.5, "change_pct": 0.12},
      ...
    }
    """
    result = {}
    for currency, ticker in FX_TICKERS.items():
        today, prev = _get_close_and_prev(ticker)
        result[currency] = {
            "rate": today,
            "change_pct": _pct_change(today, prev),
        }
    return result


def fetch_gold_krw(usd_krw_rate: float | None = None) -> dict:
    """
    순금 시세 (원/그램) 반환
    {
      "price_krw": 119500.0,   # 원/g
      "price_usd": 3150.0,     # USD/oz
      "change_pct": 0.45,
    }
    """
    today_oz, prev_oz = _get_close_and_prev("GC=F")  # 금 선물 (USD/oz)

    # USD/KRW 환율
    if usd_krw_rate is None:
        usd_today, _ = _get_close_and_prev("USDKRW=X")
        usd_krw_rate = usd_today

    price_krw = None
    if today_oz is not None and usd_krw_rate is not None:
        price_krw = (today_oz / TROY_OZ_TO_GRAM) * usd_krw_rate

    return {
        "price_krw": price_krw,
        "price_usd": today_oz,
        "change_pct": _pct_change(today_oz, prev_oz),
    }


def fetch_stock(ticker_str: str) -> dict:
    """
    단일 종목 시세 반환
    {
      "ticker": "005930.KS",
      "name": "삼성전자",
      "price": 72400.0,
      "currency": "KRW",
      "change_abs": 800.0,
      "change_pct": 1.12,
      "error": None,
    }
    """
    today, prev = _get_close_and_prev(ticker_str)

    if today is None:
        return {
            "ticker": ticker_str,
            "name": ticker_str,
            "price": None,
            "currency": "",
            "change_abs": None,
            "change_pct": None,
            "error": "데이터를 가져올 수 없습니다. 종목 코드를 확인하세요.",
        }

    try:
        tk = yf.Ticker(ticker_str)
        info = tk.fast_info
        name = getattr(info, "description", None) or ticker_str
        currency = getattr(info, "currency", "") or ""
        # fast_info에 이름이 없으면 info dict 시도
        if name == ticker_str:
            full_info = tk.info
            name = full_info.get("longName") or full_info.get("shortName") or ticker_str
            if not currency:
                currency = full_info.get("currency", "")
    except Exception:
        name = ticker_str
        currency = ""

    return {
        "ticker": ticker_str,
        "name": name,
        "price": today,
        "currency": currency,
        "change_abs": (today - prev) if prev is not None else None,
        "change_pct": _pct_change(today, prev),
        "error": None,
    }


def resolve_ticker(raw: str, market: str) -> str | None:
    """
    사용자 입력 → 실제 티커 문자열 변환
    - 이미 접미사가 붙어 있으면 그대로 사용
    - 없으면 해당 시장의 접미사를 순서대로 시도
    """
    raw = raw.strip().upper()
    if not raw:
        return None

    market_cfg = MARKET_INFO.get(market, {})
    suffixes = market_cfg.get("suffixes", [""])

    # 이미 dot(.)이 포함되어 있으면 그대로
    if "." in raw or not suffixes or suffixes == [""]:
        return raw

    # 접미사 순서대로 시도
    for suffix in suffixes:
        candidate = raw + suffix
        today, _ = _get_close_and_prev(candidate)
        if today is not None:
            return candidate

    # 모두 실패하면 첫 번째 접미사 붙여서 반환 (에러 메시지용)
    return raw + suffixes[0]
