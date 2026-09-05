RiskLens Demo

Binance Agent OS Mini Hackathon — Track A

RiskLens is an AI-powered market-risk analysis prototype designed around Binance Agent OS.

It combines Binance market data with multi-timeframe analysis to turn raw market information into a structured risk report.

Demo Workflow

1. Retrieve live BTCUSDT market data.
2. Examine the 15m, 1h, and 4h timeframes.
3. Compare bullish and bearish candle direction across timeframes.
4. Calculate open-to-close momentum for the latest completed candle.
5. Identify recent support and resistance using the latest completed 4h candles.
6. Produce a risk level, confidence level, and market outlook.
7. Highlight mixed signals instead of forcing a trade decision.

Demo Prompt

Using Binance market data, run RiskLens analysis on BTCUSDT across the 15m, 1h and 4h timeframes.

Compare the latest completed candle direction on each timeframe, calculate the open-to-close momentum, identify recent support and resistance from the latest completed 4h candles, and provide the resulting risk level, confidence, and market outlook.

Do not invent missing information.

Example Output

RiskLens produces a structured report containing:

- Current BTCUSDT price
- 15m market direction
- 1h market direction
- 4h market direction
- Momentum for each timeframe
- Recent support
- Recent resistance
- Risk level
- Confidence
- Market outlook

Key Idea

RiskLens does not blindly tell a trader to buy or sell.

It organizes live market information into a simple multi-timeframe risk brief so that a human can make a more informed decision.

Technical Architecture

The prototype uses Binance public market-data APIs for its live BTCUSDT data and automated testing.

The project is designed around Binance Agent OS as the AI-agent connection layer for the hackathon.

Project Files

- "risklens_agent.py" — main agent/report layer
- "risklens_analyzer.py" — multi-timeframe risk-analysis logic
- "risklens_binance.py" — Binance market-data functions
- ".github/workflows/python-package-conda.yml" — automated test workflow

Disclaimer

RiskLens is an experimental hackathon project for educational and research purposes. Market analysis is uncertain and is not financial advice or a guarantee of trading results.
