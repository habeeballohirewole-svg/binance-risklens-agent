"""
RiskLens — Binance Agent OS Risk Analysis Agent

RiskLens combines Binance market data with multi-timeframe
risk analysis to produce a structured market intelligence report.
"""

from risklens_analyzer import analyze
from risklens_binance import get_market_snapshot


def run_risklens():
    """Run a RiskLens market-risk assessment."""

    snapshot = get_market_snapshot()
    result = analyze(snapshot)

    return {
        "agent": "RiskLens",
        "exchange": "Binance",
        "symbol": result["symbol"],
        "price": result["price"],
        "signals": result["signals"],
        "changes": result["changes"],
        "support": result["support"],
        "resistance": result["resistance"],
        "risk_level": result["risk_level"],
        "confidence": result["confidence"],
        "outlook": result["outlook"],
    }


def format_report(result):
    """Create a structured human-readable RiskLens report."""

    lines = [
        "=== RiskLens Agent Report ===",
        f"Exchange: {result['exchange']}",
        f"Symbol: {result['symbol']}",
        f"Current price: {result['price']}",
        "",
        "Multi-timeframe signals:",
    ]

    for signal in result["signals"]:
        lines.append(f"- {signal}")

    lines.append("")
    lines.append("Momentum:")

    for timeframe, change in result["changes"].items():
        lines.append(f"- {timeframe}: {change:.4f}%")

    lines.extend(
        [
            "",
            f"Support: {result['support']}",
            f"Resistance: {result['resistance']}",
            "",
            f"Risk level: {result['risk_level']}",
            f"Confidence: {result['confidence']}",
            f"Outlook: {result['outlook']}",
        ]
    )

    return "\n".join(lines)


if __name__ == "__main__":
    result = run_risklens()
    print(format_report(result))
