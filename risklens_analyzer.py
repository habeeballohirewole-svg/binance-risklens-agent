"""
RiskLens — Simple BTCUSDT risk analyzer

Reads live Binance market data and produces a basic
multi-timeframe risk assessment.
"""

from risklens_binance import get_market_snapshot


def analyze(snapshot):
    price = snapshot["current_price"]

    candles_15m = snapshot["15m"]
    candles_1h = snapshot["1h"]
    candles_4h = snapshot["4h"]

    c15 = candles_15m[-1]
    c1h = candles_1h[-1]
    c4h = candles_4h[-1]

    signals = []

    # 15-minute direction
    if c15["close"] > c15["open"]:
        signals.append("15m bullish")
    else:
        signals.append("15m bearish")

    # 1-hour direction
    if c1h["close"] > c1h["open"]:
        signals.append("1h bullish")
    else:
        signals.append("1h bearish")

    # 4-hour direction
    if c4h["close"] > c4h["open"]:
        signals.append("4h bullish")
    else:
        signals.append("4h bearish")

    bullish = sum("bullish" in signal for signal in signals)
    bearish = sum("bearish" in signal for signal in signals)

    if bullish == 3:
        risk = "LOW"
        outlook = "Bullish alignment"
    elif bearish == 3:
        risk = "HIGH"
        outlook = "Bearish alignment"
    else:
        risk = "MEDIUM"
        outlook = "Mixed signals"

    return {
        "symbol": "BTCUSDT",
        "price": price,
        "signals": signals,
        "risk_level": risk,
        "outlook": outlook,
    }


if __name__ == "__main__":
    snapshot = get_market_snapshot()
    result = analyze(snapshot)

    print("\n=== RiskLens BTCUSDT Analysis ===")
    print(f"Current price: {result['price']}")
    print(f"15m: {result['signals'][0]}")
    print(f"1h:  {result['signals'][1]}")
    print(f"4h:  {result['signals'][2]}")
    print(f"Risk level: {result['risk_level']}")
    print(f"Outlook: {result['outlook']}")
