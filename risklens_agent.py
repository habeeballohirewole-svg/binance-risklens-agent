"""
RiskLens — Binance Agent OS Risk Analysis Agent

RiskLens is an AI-agent layer for Binance market intelligence.
It combines Binance market data with simple multi-timeframe
risk analysis to help users understand market conditions.

The Binance Agent OS MCP endpoint can provide market information
to the AI agent, while this module contains the RiskLens analysis
logic.
"""

from risklens_analyzer import analyze
from risklens_binance import get_market_snapshot


def run_risklens():
    """
    Run a RiskLens market-risk assessment using Binance data.
    """

    snapshot = get_market_snapshot()
    result = analyze(snapshot)

    return {
        "agent": "RiskLens",
        "exchange": "Binance",
        "symbol": result["symbol"],
        "price": result["price"],
        "signals": result["signals"],
        "risk_level": result["risk_level"],
        "outlook": result["outlook"],
    }


def format_report(result):
    """Create a human-readable RiskLens report."""

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

    lines.extend(
        [
            "",
            f"Risk level: {result['risk_level']}",
            f"Outlook: {result['outlook']}",
        ]
    )

    return "\n".join(lines)


if __name__ == "__main__":
    report = run_risklens()
    print(format_report(report))
