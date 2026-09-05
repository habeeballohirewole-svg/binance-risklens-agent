Binance RiskLens Agent

RiskLens is a Track A hackathon prototype built around Binance Agent OS.

It is an AI-powered market-risk analysis agent that turns Binance market data into a structured, disciplined trading research report.

What RiskLens does

Given a market such as BTCUSDT, RiskLens can:

1. Access live Binance market information through Binance's public market-data API, while the project is designed to integrate with Binance Agent OS as its AI-agent connection layer.
2. Examine multiple timeframes, including 15m, 1h, and 4h.
3. Compare short-, medium-, and higher-timeframe market direction.
4. Identify whether signals are aligned or mixed.
5. Produce a clear risk level and market outlook.
6. Highlight uncertainty instead of inventing missing information.
7. Provide analysis for research and decision support rather than blindly executing trades.

Binance Agent OS integration

RiskLens is designed to use Binance Agent OS as the AI-agent connection layer, while the current prototype uses Binance's public market-data API for live BTCUSDT data and automated testing.

https://agent.binance.com/mcp/agentic

The MCP connection allows the AI agent to access Binance market information and use it as the live data layer for RiskLens analysis.

Architecture

User → RiskLens AI Agent → Binance Agent OS / MCP → Binance Market Data → RiskLens Multi-Timeframe Analysis → Structured Risk Report
Example

A user can ask:

«Using Binance Agent OS, analyze BTCUSDT across the 15m, 1h and 4h timeframes.»

RiskLens can return:

- Current BTCUSDT price
- Multi-timeframe market signals
- Risk level
- Market outlook
- Key observations
- Clear uncertainty when data is insufficient

Project files

risklens_agent.py

The main RiskLens agent layer. It combines the market-data layer with the RiskLens analysis engine and produces a structured report.

risklens_analyzer.py

Contains the multi-timeframe risk-analysis logic.

risklens_binance.py

Contains the Binance market-data functions used by the prototype and automated tests.

demo/DEMO_SCRIPT.md

Contains the planned demonstration flow for presenting RiskLens.

Testing

The repository includes a GitHub Actions workflow that automatically tests the RiskLens analysis code.

The workflow verifies that the project can retrieve Binance market data and successfully produce a RiskLens analysis.

Design principles

Risk first

RiskLens focuses on understanding market conditions before discussing a trading setup.

Multi-timeframe confirmation

Signals are compared across multiple timeframes rather than relying on a single candle.

No fabricated data

If required information is unavailable, RiskLens should clearly state the limitation instead of making up values.

Human decision support

RiskLens is designed to assist traders with market research. It does not encourage blind execution or guarantee profits.

Hackathon Track

Binance Agent OS Mini Hackathon — Track A

RiskLens demonstrates how an AI agent can use Binance Agent OS as a market-data connection layer and transform that information into useful, structured risk intelligence.

Disclaimer

RiskLens is an experimental hackathon project for educational and research purposes. Market analysis is uncertain and should not be considered financial advice or a guarantee of trading results.
