# Binance RiskLens Agent

A hackathon-ready Track A prototype for Binance Agent OS.

## What it does

RiskLens is an AI market-analysis agent designed to turn Binance market data into a disciplined trading research report.

Given a symbol such as BTCUSDT, it:
1. Pulls live Binance market data through the Binance Agent OS MCP connection.
2. Examines multiple timeframes.
3. Identifies trend, momentum, support/resistance and volatility.
4. Produces a structured setup with entry zones, invalidation and risk/reward.
5. Refuses to manufacture missing data and clearly labels uncertainty.
6. Never places an order unless the user explicitly asks and the connected permissions allow it.

## Agent OS connection

The project is configured for the official Binance MCP endpoint:

`https://agent.binance.com/mcp/agentic`

Binance states that Agent OS can connect AI agents to Binance market data and trading capabilities, with permissions controlled by the user.

## Quick start

This repo is intended to be opened in a supported agent environment such as Claude Code, Codex, ChatGPT or VS Code.

1. Open the project.
2. Connect/authenticate the Binance MCP server.
3. Load `AGENTS.md` as the agent's operating instructions.
4. Ask:

   `Run a RiskLens analysis on BTCUSDT using 15m, 1h and 4h.`

For the hackathon demo, keep the agent in read-only/analysis mode.

## Example demo prompts

- `Analyze BTCUSDT with RiskLens.`
- `Compare ETHUSDT and SOLUSDT and rank them by setup quality.`
- `What would invalidate the current BTCUSDT thesis?`
- `Give me a conservative setup and explain the risk.`
- `Re-run the analysis and tell me what changed.`

## Safety design

RiskLens is analysis-first. It does not assume that an AI signal is financial advice. It does not invent prices, indicators or order-book information. Trade execution should remain disabled for the demo unless explicitly authorized.

## Hackathon pitch

**RiskLens — from market noise to a disciplined decision brief.**

Most trading assistants answer questions. RiskLens follows a repeatable workflow: collect live data → cross-check timeframes → score the setup → expose invalidation → communicate uncertainty.

This makes the agent useful even when the correct action is **do nothing**.
