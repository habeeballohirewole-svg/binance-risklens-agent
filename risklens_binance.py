"""
RiskLens — Binance market-data connector

Uses Binance public REST APIs (read-only).
No API key, account access, or trading permission is required.
"""

import json
import urllib.parse
import urllib.request


BINANCE_API = "https://api1.binance.com"


def get_json(path, params=None):
    """Fetch JSON from Binance's public API."""
    params = params or {}
    query = urllib.parse.urlencode(params)
    url = f"{BINANCE_API}{path}"
    if query:
        url += f"?{query}"

    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def get_btcusdt_price():
    """Get the current BTCUSDT spot price."""
    data = get_json(
        "/api/v3/ticker/price",
        {"symbol": "BTCUSDT"},
    )
    return float(data["price"])


def get_btcusdt_candles(interval, limit=1):
    """Get the latest BTCUSDT candlestick data."""
    data = get_json(
        "/api/v3/klines",
        {
            "symbol": "BTCUSDT",
            "interval": interval,
            "limit": limit,
        },
    )

    candles = []

    for candle in data:
        candles.append(
            {
                "open_time": candle[0],
                "open": float(candle[1]),
                "high": float(candle[2]),
                "low": float(candle[3]),
                "close": float(candle[4]),
                "volume": float(candle[5]),
            }
        )

    return candles


def get_market_snapshot():
    """Return a simple multi-timeframe BTCUSDT market snapshot."""
    return {
        "symbol": "BTCUSDT",
        "current_price": get_btcusdt_price(),
        "15m": get_btcusdt_candles("15m"),
        "1h": get_btcusdt_candles("1h"),
        "4h": get_btcusdt_candles("4h"),
    }


if __name__ == "__main__":
    snapshot = get_market_snapshot()
    print(json.dumps(snapshot, indent=2))
