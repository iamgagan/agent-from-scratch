# AI Investment Planner

An AI-powered multi-agent system that helps investors analyze their current portfolio, understand market trends, receive tailored investment ideas, optimize taxes, and build long-term financial plans geared toward generational wealth.

> **Disclaimer**  
> This project is for educational and demonstration purposes only.  
> It does **not** provide personalized financial, investment, or tax advice.  
> Always consult qualified professionals before taking action.

---

## Features

* **Portfolio Analyzer** – breaks down allocation, performance, risk, and diversification.
* **Market Trends Analyst** – explains real-time (mock) macro and sector conditions.
* **Recommendation Specialist** – suggests stocks, ETFs, bonds, alternatives aligned with risk, horizon, and goals.
* **Tax Optimization Specialist** – summarizes strategies such as tax-loss harvesting and asset location.
* **Financial Planning Specialist** – projects retirement outcomes and milestone targets with dynamic glide-paths.
* **Multi-Agent Orchestration** – the top-level *Investment Planner* agent routes the conversation to specialists via transfer functions.
* **Interactive CLI & Demo Menu** – explore single-topic demos or an open chat loop.
* **Extensible Functions** – plug in real brokerage, data, or ML models by replacing the mock helpers.
* **Clear Disclaimers** – every recommendation or strategy callout reminds users of the educational scope.

---

## Architecture

```
User ↔ Investment Planner (router)
              ├── Portfolio Analyzer ── analyze_portfolio()
              ├── Market Trends Analyst ── get_market_data()
              ├── Recommendation Specialist ── get_investment_recommendations()
              ├── Tax Optimization Specialist ── get_tax_optimization_strategies()
              └── Financial Planning Specialist ── create_financial_plan()
```

* **agent-from-scratch Core** – provides `Agent`, `Swarm`, tool-calling, and parallel function execution.
* **Specialist Agents** – each owns domain instructions + callable Python functions (tools).
* **Transfer Functions** – zero-shot delegate to another agent when deeper expertise is needed.
* **Mock Data Layer** – deterministic sample datasets decouple the UI from paid data feeds; swap with live APIs later.
* **Conversation History** – maintained in memory via `Swarm.run`, enabling multi-turn context.

### Directory Structure

```
.
├── agent.py                         # framework (upstream repo)
├── investment_planner.py            # main multi-agent implementation
├── demo_investment_planner.py       # guided demo & interactive menu
├── requirements.txt
└── AI_INVESTMENT_PLANNER_README.md  # (this file)
```

---

## Getting Started

### Prerequisites

1. Python 3.10+
2. An OpenAI API key (`OPENAI_API_KEY`) – required for language generation.
3. `pip` / `venv` for dependency isolation.

### Installation

```bash
git clone https://github.com/your-org/ai-investment-planner.git
cd ai-investment-planner
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.template .env         # add OPENAI_API_KEY inside
```

### Running the Demo

```bash
python demo_investment_planner.py
```

Follow the numbered menu to:

* run standalone demonstrations (portfolio, market, etc.),
* watch agents transfer control in the multi-agent showcase, or
* enter **Interactive Mode** for free-form Q&A.

### Quick Interactive Example

```bash
python investment_planner.py
# Sample session
User: I'd like to retire by 60 with $2M. Can you craft a plan?
Investment Planner: Sure! Transferring you to Financial Planning Specialist...
Financial Planning Specialist: [detailed projection]
```

---

## Customising & Extending

| Area                | How to Extend                                  |
|---------------------|------------------------------------------------|
| Data Sources        | Replace `get_market_data` with real API calls (e.g., Alpha Vantage, IEX, FRED). |
| Brokerage Linking   | Add OAuth + brokerage SDK to pull holdings into `analyze_portfolio`. |
| Machine Learning    | Train return-forecast or risk models and call them from specialist agents. |
| Persistence         | Store chats, plans, and user profiles in a database for recall. |
| Front-end           | Wrap the planners in a React / Streamlit UI.   |

---

## Limitations

* **Mock Data** – current helpers return static examples; not suitable for live trading.
* **No Order Execution** – the system stops at *recommendations*, it cannot place trades.
* **Regulatory Compliance** – lacks KYC/AML checks and formal registration required for public advisory services.
* **Latent Model Hallucinations** – large language models may invent facts; cross-validate outputs.
* **Single-User Memory** – no persistent user store; new sessions start fresh.

---

## Roadmap

1. Live data adapters (IEX Cloud, Polygon, SEC filings).
2. Portfolio importers for major brokerages via Plaid/Finnhub.
3. Back-testing & Monte Carlo simulation module.
4. Persistent vector memory for long-term user profiles.
5. Web dashboard with rich charts (Plotly, ECharts).
6. Compliance & audit logging layer.
7. Fine-tune domain specialist models or RAG with financial research papers.
8. Automated rebalancing simulator and tax-aware withdrawal engine.

---

### Contributing

Pull requests are welcome! Please open an issue to discuss major changes or new agent modules.

### License

MIT © 2025 Your Name / Organization
