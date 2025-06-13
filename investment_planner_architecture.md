# AI Investment Planner Architecture

This document outlines the architecture of the AI Investment Planner system, showing the relationships between the main investment planner agent and the specialized agents, as well as the flow of data and function calls.

## System Architecture Diagram

flowchart TD
    User([User]) <--> IP[Investment Planner Agent]
    
    IP -->|transfer_to_portfolio_analysis| PA[Portfolio Analyzer]
    IP -->|transfer_to_market_trends| MT[Market Trends Analyst]
    IP -->|transfer_to_recommendation| RS[Recommendation Specialist]
    IP -->|transfer_to_tax_specialist| TS[Tax Optimization Specialist]
    IP -->|transfer_to_financial_planning| FP[Financial Planning Specialist]
    
    PA -->|transfer_back| IP
    MT -->|transfer_back| IP
    RS -->|transfer_back| IP
    TS -->|transfer_back| IP
    FP -->|transfer_back| IP
    
    PA -->|analyze_portfolio| PD[(Portfolio Data)]
    MT -->|get_market_data| MD[(Market Data)]
    RS -->|get_investment_recommendations| RD[(Recommendation Data)]
    TS -->|get_tax_optimization_strategies| TD[(Tax Strategy Data)]
    FP -->|create_financial_plan| FD[(Financial Plan Data)]
    
    PA -.->|transfer_to_market_trends| MT
    PA -.->|transfer_to_recommendation| RS
    PA -.->|transfer_to_tax_specialist| TS
    PA -.->|transfer_to_financial_planning| FP
    
    MT -.->|transfer_to_portfolio_analysis| PA
    MT -.->|transfer_to_recommendation| RS
    MT -.->|transfer_to_tax_specialist| TS
    MT -.->|transfer_to_financial_planning| FP
    
    RS -.->|transfer_to_portfolio_analysis| PA
    RS -.->|transfer_to_market_trends| MT
    RS -.->|transfer_to_tax_specialist| TS
    RS -.->|transfer_to_financial_planning| FP
    
    TS -.->|transfer_to_portfolio_analysis| PA
    TS -.->|transfer_to_market_trends| MT
    TS -.->|transfer_to_recommendation| RS
    TS -.->|transfer_to_financial_planning| FP
    
    FP -.->|transfer_to_portfolio_analysis| PA
    FP -.->|transfer_to_market_trends| MT
    FP -.->|transfer_to_recommendation| RS
    FP -.->|transfer_to_tax_specialist| TS
    
    classDef mainAgent fill:#4672b4,color:white,stroke:#333,stroke-width:1px
    classDef specialistAgent fill:#47956f,color:white,stroke:#333,stroke-width:1px
    classDef dataStore fill:#de953e,color:white,stroke:#333,stroke-width:1px
    classDef user fill:#8b251e,color:white,stroke:#333,stroke-width:1px
    
    class IP mainAgent
    class PA,MT,RS,TS,FP specialistAgent
    class PD,MD,RD,TD,FD dataStore
    class User user

## Architecture Components

### Main Router Agent
- **Investment Planner Agent**: Central coordinator that routes user queries to specialized agents based on the nature of the request.

### Specialist Agents
1. **Portfolio Analyzer**: Analyzes investment portfolios and provides detailed insights on allocation, risk, and performance.
2. **Market Trends Analyst**: Identifies and explains market patterns and economic indicators.
3. **Recommendation Specialist**: Provides tailored investment suggestions based on user goals and risk tolerance.
4. **Tax Optimization Specialist**: Suggests tax-efficient investment approaches and strategies.
5. **Financial Planning Specialist**: Creates comprehensive financial plans with clear milestones for long-term wealth building.

### Data Functions
- **analyze_portfolio()**: Processes portfolio data to generate insights on allocation, performance, and risk.
- **get_market_data()**: Retrieves current market trends and economic indicators.
- **get_investment_recommendations()**: Generates personalized investment suggestions.
- **get_tax_optimization_strategies()**: Provides tax efficiency recommendations.
- **create_financial_plan()**: Builds long-term financial projections and milestone plans.

### Agent Transfer System
- Each agent can transfer control to any other specialist agent when a query requires different expertise.
- Solid arrows represent primary routing from the main agent.
- Dotted arrows represent inter-specialist transfers.
- All specialists can transfer back to the main Investment Planner agent.

### Data Flow
1. User query enters the system through the Investment Planner Agent
2. Investment Planner routes to appropriate specialist
3. Specialist calls relevant data functions
4. Results are processed and returned to the user
5. If needed, conversation transfers to another specialist for additional analysis

This architecture enables a comprehensive approach to investment planning, allowing the system to handle complex queries that span multiple domains of financial expertise.
