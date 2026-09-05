"""
RiskLens — Multi-Timeframe Binance Market Risk Analyzer

Analyzes BTCUSDT across 15m, 1h, and 4h timeframes and produces
a structured market-risk assessment.
"""

from risklens_binance import get_market_snapshot


def candle_direction(candle):
    """Return bullish or bearish based on the candle body."""
    if candle["close"] > candle["open"]:
        return "bullish"
    return "bearish"


def calculate_change(candle):
    """Calculate percentage change from candle open to close."""
    if candle["open"] == 0:
        return 0.0

    return ((candle["close"] - candle["open"]) / candle["open"]) * 100


def analyze(snapshot):
    """Analyze Binance market data across multiple timeframes."""

    price = snapshot["current_price"]

    candles_15m = snapshot["15m"]
    candles_1h = snapshot["1h"]
    candles_4h = snapshot["4h"]

        c15 = candles_15m[-2]
    c1h = candles_1h[-2]
    c4h = candles_4h[-2]

    signals = []

    # Multi-timeframe direction
    directions = {
        "15m": candle_direction(c15),
        "1h": candle_direction(c1h),
        "4h": candle_direction(c4h),
    }

    for timeframe, direction in directions.items():
        signals.append(f"{timeframe} {direction}")

    bullish_count = sum(
        direction == "bullish" for direction in directions.values()
    )
    bearish_count = sum(
        direction == "bearish" for direction in directions.values()
    )

    # Determine overall market alignment
    if bullish_count == 3:
        risk_level = "LOW"
        outlook = "Strong bullish alignment"
        confidence = "HIGH"
    elif bearish_count == 3:
        risk_level = "HIGH"
        outlook = "Strong bearish alignment"
        confidence = "HIGH"
    elif bullish_count > bearish_count:
        risk_level = "MEDIUM"
        outlook = "Bullish bias with mixed confirmation"
        confidence = "MEDIUM"
    elif bearish_count > bullish_count:
        risk_level = "HIGH"
        outlook = "Bearish bias with mixed confirmation"
        confidence = "MEDIUM"
    else:
        risk_level = "MEDIUM"
        outlook = "Mixed market conditions"
        confidence = "LOW"

    # Candle momentum
    changes = {
        "15m": calculate_change(c15),
        "1h": calculate_change(c1h),
        "4h": calculate_change(c4h),
    }

    # Recent support and resistance from available 4h candles
    recent_4h = candles_4h[-10:]

    support = min(candle["low"] for candle in recent_4h)
    resistance = max(candle["high"] for candle in recent_4h)

    return {
        "symbol": "BTCUSDT",
        "price": price,
        "signals": signals,
        "changes": changes,
        "support": support,
        "resistance": resistance,
        "risk_level": risk_level,
        "confidence": confidence,
        "outlook": outlook,
    }


if __name__ == "__main__":
    snapshot = get_market_snapshot()
    result = analyze(snapshot)

    print("\n=== RiskLens BTCUSDT Analysis ===")
    print(f"Current price: {result['price']}")

    print("\nMulti-timeframe signals:")
    for signal in result["signals"]:
        print(f"- {signal}")

    print("\nMomentum:")
    for timeframe, change in result["changes"].items():
        print(f"- {timeframe}: {change:.4f}%")

    print(f"\nSupport: {result['support']}")
    print(f"Resistance: {result['resistance']}")

    print(f"\nRisk level: {result['risk_level']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Outlook: {result['outlook']}")
