from dotenv import load_dotenv
_ = load_dotenv()

import json
import datetime
import random
from typing import Dict, List, Any

from agent import Agent, Swarm, pretty_print_messages

# Mock data functions - in a real implementation, these would connect to financial APIs
def get_market_data(sector: str = None, timeframe: str = "1month"):
    """
    Get market data for a specific sector or the overall market.
    
    Args:
        sector: The market sector to analyze (tech, healthcare, finance, energy, etc.)
        timeframe: The timeframe to analyze (1day, 1week, 1month, 3months, 1year)
    
    Returns:
        JSON string with market trend data
    """
    sectors = {
        "tech": {"trend": "bullish", "volatility": "high", "growth_potential": 8.5},
        "healthcare": {"trend": "neutral", "volatility": "medium", "growth_potential": 5.2},
        "finance": {"trend": "bearish", "volatility": "medium", "growth_potential": 3.1},
        "energy": {"trend": "bullish", "volatility": "high", "growth_potential": 7.8},
        "consumer": {"trend": "neutral", "volatility": "low", "growth_potential": 4.3},
        "real_estate": {"trend": "bearish", "volatility": "medium", "growth_potential": 2.9},
        "utilities": {"trend": "neutral", "volatility": "low", "growth_potential": 3.5},
    }
    
    market_overview = {
        "overall_trend": "neutral",
        "volatility_index": 22.5,
        "interest_rates": {"current": 4.5, "trend": "stable"},
        "inflation": {"current": 3.2, "trend": "decreasing"},
        "economic_outlook": "moderate growth",
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    if sector and sector in sectors:
        return json.dumps({
            "sector": sector,
            "data": sectors[sector],
            "market_overview": market_overview,
            "timeframe": timeframe
        })
    else:
        return json.dumps({
            "sectors": sectors,
            "market_overview": market_overview,
            "timeframe": timeframe
        })

def analyze_portfolio(portfolio: Dict[str, Any] = None):
    """
    Analyze a user's investment portfolio.
    
    Args:
        portfolio: A dictionary containing the user's portfolio information
                  If None, a sample portfolio will be used
    
    Returns:
        JSON string with portfolio analysis
    """
    if not portfolio:
        # Sample portfolio for demonstration
        portfolio = {
            "stocks": [
                {"symbol": "AAPL", "shares": 10, "purchase_price": 150.00, "current_price": 175.50},
                {"symbol": "MSFT", "shares": 5, "purchase_price": 250.00, "current_price": 280.75},
                {"symbol": "GOOGL", "shares": 3, "purchase_price": 2100.00, "current_price": 1950.25},
                {"symbol": "AMZN", "shares": 2, "purchase_price": 3200.00, "current_price": 3450.00}
            ],
            "etfs": [
                {"symbol": "SPY", "shares": 15, "purchase_price": 400.00, "current_price": 420.50},
                {"symbol": "QQQ", "shares": 8, "purchase_price": 350.00, "current_price": 375.25}
            ],
            "bonds": [
                {"name": "Treasury Bond", "value": 10000, "yield": 3.5, "maturity": "2030-01-01"},
                {"name": "Corporate Bond", "value": 5000, "yield": 4.2, "maturity": "2025-06-15"}
            ],
            "cash": 15000
        }
    
    # Calculate portfolio metrics
    total_value = 0
    stock_value = 0
    etf_value = 0
    bond_value = 0
    
    for stock in portfolio["stocks"]:
        stock_value += stock["shares"] * stock["current_price"]
    
    for etf in portfolio["etfs"]:
        etf_value += etf["shares"] * etf["current_price"]
    
    for bond in portfolio["bonds"]:
        bond_value += bond["value"]
    
    total_value = stock_value + etf_value + bond_value + portfolio["cash"]
    
    # Calculate allocation percentages
    allocation = {
        "stocks": round((stock_value / total_value) * 100, 2),
        "etfs": round((etf_value / total_value) * 100, 2),
        "bonds": round((bond_value / total_value) * 100, 2),
        "cash": round((portfolio["cash"] / total_value) * 100, 2)
    }
    
    # Calculate performance metrics
    stock_performance = []
    for stock in portfolio["stocks"]:
        gain_loss = ((stock["current_price"] - stock["purchase_price"]) / stock["purchase_price"]) * 100
        stock_performance.append({
            "symbol": stock["symbol"],
            "gain_loss_percent": round(gain_loss, 2),
            "gain_loss_value": round((stock["current_price"] - stock["purchase_price"]) * stock["shares"], 2)
        })
    
    etf_performance = []
    for etf in portfolio["etfs"]:
        gain_loss = ((etf["current_price"] - etf["purchase_price"]) / etf["purchase_price"]) * 100
        etf_performance.append({
            "symbol": etf["symbol"],
            "gain_loss_percent": round(gain_loss, 2),
            "gain_loss_value": round((etf["current_price"] - etf["purchase_price"]) * etf["shares"], 2)
        })
    
    # Risk assessment (simplified)
    risk_score = 0
    if allocation["stocks"] > 60:
        risk_score += 3
    elif allocation["stocks"] > 40:
        risk_score += 2
    else:
        risk_score += 1
        
    if allocation["bonds"] < 20:
        risk_score += 1
    
    risk_level = "High" if risk_score >= 3 else "Medium" if risk_score == 2 else "Low"
    
    return json.dumps({
        "total_value": round(total_value, 2),
        "allocation": allocation,
        "stock_performance": stock_performance,
        "etf_performance": etf_performance,
        "risk_assessment": {
            "risk_level": risk_level,
            "risk_score": risk_score,
            "diversification": "Medium" if len(portfolio["stocks"]) >= 4 else "Low"
        },
        "timestamp": datetime.datetime.now().isoformat()
    })

def get_investment_recommendations(risk_profile: str = "moderate", investment_horizon: str = "long_term", goals: List[str] = None):
    """
    Get investment recommendations based on risk profile and investment horizon.
    
    Args:
        risk_profile: The user's risk profile (conservative, moderate, aggressive)
        investment_horizon: The investment time horizon (short_term, medium_term, long_term)
        goals: List of investment goals (retirement, college_fund, house, passive_income, etc.)
    
    Returns:
        JSON string with investment recommendations
    """
    if goals is None:
        goals = ["growth"]
    
    # Define recommendation templates based on risk profile and horizon
    recommendations = {
        "conservative": {
            "short_term": {
                "allocation": {"stocks": 20, "bonds": 60, "cash": 20, "alternative": 0},
                "focus": "capital preservation",
                "stock_style": "large-cap, dividend-paying",
                "bond_style": "short-term, high-quality"
            },
            "medium_term": {
                "allocation": {"stocks": 30, "bonds": 60, "cash": 5, "alternative": 5},
                "focus": "income generation with moderate growth",
                "stock_style": "blue-chip, dividend growth",
                "bond_style": "intermediate-term, mixed quality"
            },
            "long_term": {
                "allocation": {"stocks": 40, "bonds": 50, "cash": 0, "alternative": 10},
                "focus": "income and growth",
                "stock_style": "dividend aristocrats, value stocks",
                "bond_style": "laddered approach, corporate and government"
            }
        },
        "moderate": {
            "short_term": {
                "allocation": {"stocks": 50, "bonds": 40, "cash": 10, "alternative": 0},
                "focus": "balanced growth and income",
                "stock_style": "mix of growth and value",
                "bond_style": "intermediate-term, investment grade"
            },
            "medium_term": {
                "allocation": {"stocks": 60, "bonds": 30, "cash": 5, "alternative": 5},
                "focus": "growth with some income",
                "stock_style": "quality growth, some international exposure",
                "bond_style": "corporate bonds, some high-yield"
            },
            "long_term": {
                "allocation": {"stocks": 70, "bonds": 20, "cash": 0, "alternative": 10},
                "focus": "long-term capital appreciation",
                "stock_style": "growth-oriented, global diversification",
                "bond_style": "strategic mix of duration and credit quality"
            }
        },
        "aggressive": {
            "short_term": {
                "allocation": {"stocks": 70, "bonds": 20, "cash": 10, "alternative": 0},
                "focus": "capital appreciation",
                "stock_style": "growth stocks, some speculative",
                "bond_style": "high-yield corporate"
            },
            "medium_term": {
                "allocation": {"stocks": 80, "bonds": 10, "cash": 0, "alternative": 10},
                "focus": "aggressive growth",
                "stock_style": "growth and momentum, sector bets",
                "bond_style": "high-yield, emerging markets debt"
            },
            "long_term": {
                "allocation": {"stocks": 90, "bonds": 0, "cash": 0, "alternative": 10},
                "focus": "maximum capital appreciation",
                "stock_style": "aggressive growth, emerging markets, small-cap",
                "bond_style": "minimal or strategic only"
            }
        }
    }
    
    # Get base recommendation
    if risk_profile not in recommendations:
        risk_profile = "moderate"
    if investment_horizon not in recommendations[risk_profile]:
        investment_horizon = "medium_term"
        
    base_rec = recommendations[risk_profile][investment_horizon]
    
    # Adjust for goals
    goal_adjustments = {}
    for goal in goals:
        if goal == "retirement":
            goal_adjustments["retirement"] = {
                "focus": "long-term growth transitioning to income",
                "vehicles": ["target-date funds", "index ETFs", "dividend stocks", "Roth IRA", "401(k)"]
            }
        elif goal == "college_fund":
            goal_adjustments["college_fund"] = {
                "focus": "growth with time-based de-risking",
                "vehicles": ["529 plans", "education savings accounts", "index funds"]
            }
        elif goal == "house":
            goal_adjustments["house"] = {
                "focus": "capital preservation with modest growth",
                "vehicles": ["high-yield savings", "short-term bond funds", "CDs"]
            }
        elif goal == "passive_income":
            goal_adjustments["passive_income"] = {
                "focus": "income generation",
                "vehicles": ["dividend stocks", "REITs", "preferred stocks", "bond ladder"]
            }
    
    # Generate specific stock/ETF recommendations
    stock_recommendations = []
    etf_recommendations = []
    bond_recommendations = []
    alternative_recommendations = []
    
    # This would normally come from a financial API or database
    # Using mock data for demonstration
    if base_rec["allocation"]["stocks"] > 0:
        if "conservative" in risk_profile:
            stock_recommendations = [
                {"symbol": "JNJ", "name": "Johnson & Johnson", "sector": "Healthcare", "reason": "Stable dividend aristocrat"},
                {"symbol": "PG", "name": "Procter & Gamble", "sector": "Consumer Staples", "reason": "Defensive stock with consistent dividends"},
                {"symbol": "KO", "name": "Coca-Cola", "sector": "Consumer Staples", "reason": "Strong brand and reliable dividend"}
            ]
        elif "moderate" in risk_profile:
            stock_recommendations = [
                {"symbol": "MSFT", "name": "Microsoft", "sector": "Technology", "reason": "Growth and dividend with strong fundamentals"},
                {"symbol": "HD", "name": "Home Depot", "sector": "Retail", "reason": "Solid growth and dividend increases"},
                {"symbol": "V", "name": "Visa", "sector": "Financial Services", "reason": "Strong growth in digital payments"}
            ]
        else:  # aggressive
            stock_recommendations = [
                {"symbol": "NVDA", "name": "NVIDIA", "sector": "Technology", "reason": "Exposure to AI and computing growth"},
                {"symbol": "TSLA", "name": "Tesla", "sector": "Automotive/Energy", "reason": "Innovation leader in EV and energy"},
                {"symbol": "AMZN", "name": "Amazon", "sector": "Technology/Retail", "reason": "Market leader with multiple growth vectors"}
            ]
    
    if base_rec["allocation"]["bonds"] > 0 or "ETF" in str(goals):
        if "conservative" in risk_profile:
            etf_recommendations = [
                {"symbol": "VYM", "name": "Vanguard High Dividend Yield ETF", "type": "Dividend", "reason": "Income focus with quality companies"},
                {"symbol": "SPLV", "name": "Invesco S&P 500 Low Volatility ETF", "type": "Low Volatility", "reason": "Reduced market volatility"},
                {"symbol": "VIG", "name": "Vanguard Dividend Appreciation ETF", "type": "Dividend Growth", "reason": "Companies with growing dividends"}
            ]
        elif "moderate" in risk_profile:
            etf_recommendations = [
                {"symbol": "VOO", "name": "Vanguard S&P 500 ETF", "type": "Index", "reason": "Core U.S. market exposure"},
                {"symbol": "VGT", "name": "Vanguard Information Technology ETF", "type": "Sector", "reason": "Technology sector exposure"},
                {"symbol": "VXUS", "name": "Vanguard Total International Stock ETF", "type": "International", "reason": "International diversification"}
            ]
        else:  # aggressive
            etf_recommendations = [
                {"symbol": "QQQ", "name": "Invesco QQQ Trust", "type": "Index", "reason": "Exposure to innovative NASDAQ companies"},
                {"symbol": "ARKK", "name": "ARK Innovation ETF", "type": "Active/Thematic", "reason": "Disruptive innovation exposure"},
                {"symbol": "VWO", "name": "Vanguard Emerging Markets ETF", "type": "Emerging Markets", "reason": "Growth potential in developing economies"}
            ]
    
    if base_rec["allocation"]["bonds"] > 0:
        if "conservative" in risk_profile:
            bond_recommendations = [
                {"name": "Treasury Bonds", "type": "Government", "duration": "Short to Intermediate", "reason": "Safety and stability"},
                {"name": "Municipal Bonds", "type": "Tax-exempt", "duration": "Intermediate", "reason": "Tax advantages for higher incomes"},
                {"name": "BND", "symbol": "Vanguard Total Bond Market ETF", "type": "ETF", "reason": "Broad bond market exposure"}
            ]
        elif "moderate" in risk_profile:
            bond_recommendations = [
                {"name": "Corporate Bonds (Investment Grade)", "type": "Corporate", "duration": "Intermediate", "reason": "Higher yield than government bonds"},
                {"name": "LQD", "symbol": "iShares iBoxx $ Investment Grade Corporate Bond ETF", "type": "ETF", "reason": "Quality corporate exposure"},
                {"name": "VCIT", "symbol": "Vanguard Intermediate-Term Corporate Bond ETF", "type": "ETF", "reason": "Balanced yield and duration"}
            ]
        else:  # aggressive
            bond_recommendations = [
                {"name": "High-Yield Corporate Bonds", "type": "Corporate", "duration": "Varied", "reason": "Higher income potential"},
                {"name": "HYG", "symbol": "iShares iBoxx $ High Yield Corporate Bond ETF", "type": "ETF", "reason": "Exposure to higher-yielding bonds"},
                {"name": "EMB", "symbol": "iShares J.P. Morgan USD Emerging Markets Bond ETF", "type": "ETF", "reason": "Emerging market bond exposure"}
            ]
    
    if base_rec["allocation"]["alternative"] > 0:
        alternative_recommendations = [
            {"name": "Real Estate Investment Trusts (REITs)", "type": "Real Estate", "example": "VNQ (Vanguard Real Estate ETF)", "reason": "Income and inflation hedge"},
            {"name": "Commodities", "type": "Hard Assets", "example": "PDBC (Invesco Optimum Yield Diversified Commodity Strategy ETF)", "reason": "Diversification and inflation protection"},
            {"name": "Gold", "type": "Precious Metal", "example": "GLD (SPDR Gold Shares)", "reason": "Portfolio hedge during market stress"}
        ]
    
    return json.dumps({
        "base_recommendation": base_rec,
        "goal_specific_recommendations": goal_adjustments,
        "specific_investments": {
            "stocks": stock_recommendations,
            "etfs": etf_recommendations,
            "bonds": bond_recommendations,
            "alternatives": alternative_recommendations
        },
        "disclaimer": "These recommendations are for educational purposes only and do not constitute financial advice. Please consult with a financial advisor before making investment decisions."
    })

def get_tax_optimization_strategies(income_bracket: str = "middle", account_types: List[str] = None):
    """
    Get tax optimization strategies for investments.
    
    Args:
        income_bracket: The user's income bracket (low, middle, high, very_high)
        account_types: List of account types the user has (401k, ira, roth_ira, brokerage, hsa, etc.)
    
    Returns:
        JSON string with tax optimization strategies
    """
    if account_types is None:
        account_types = ["brokerage"]
    
    strategies = {
        "account_placement": {
            "tax_advantaged_accounts": {
                "recommendation": "Place tax-inefficient investments in tax-advantaged accounts",
                "examples": [
                    "REITs in Roth IRA",
                    "Bond funds in Traditional IRA",
                    "High-turnover funds in 401(k)"
                ]
            },
            "taxable_accounts": {
                "recommendation": "Place tax-efficient investments in taxable accounts",
                "examples": [
                    "Index ETFs",
                    "Growth stocks held long-term",
                    "Municipal bonds (if applicable)"
                ]
            }
        },
        "tax_loss_harvesting": {
            "description": "Selling investments at a loss to offset capital gains",
            "considerations": [
                "Wash sale rules (30-day waiting period)",
                "Annual limit on deductible losses against ordinary income ($3,000)",
                "Long-term vs. short-term considerations"
            ]
        },
        "tax_gain_harvesting": {
            "description": "Selling investments with gains strategically",
            "considerations": [
                "0% long-term capital gains rate for lower income brackets",
                "Resetting cost basis",
                "Coordinating with other income"
            ]
        },
        "retirement_account_strategies": {}
    }
    
    # Add income-specific strategies
    if income_bracket == "low":
        strategies["income_specific"] = {
            "focus": "Tax credits and deductions",
            "strategies": [
                "Retirement Savings Contribution Credit (Saver's Credit)",
                "Maximize Roth contributions (tax-free growth)",
                "Consider tax-exempt municipal bonds for taxable accounts"
            ]
        }
    elif income_bracket == "middle":
        strategies["income_specific"] = {
            "focus": "Balance between pre-tax and Roth savings",
            "strategies": [
                "Split retirement savings between traditional and Roth accounts",
                "Consider Health Savings Account (HSA) as a triple-tax advantage",
                "Utilize tax-loss harvesting in taxable accounts"
            ]
        }
    elif income_bracket == "high":
        strategies["income_specific"] = {
            "focus": "Tax deferral and reduction",
            "strategies": [
                "Maximize pre-tax retirement contributions",
                "Consider backdoor Roth IRA contributions",
                "Utilize tax-loss harvesting strategically",
                "Consider exchange-traded funds over mutual funds in taxable accounts"
            ]
        }
    else:  # very_high
        strategies["income_specific"] = {
            "focus": "Advanced tax strategies",
            "strategies": [
                "Consider mega backdoor Roth if available",
                "Charitable giving strategies (donor-advised funds, appreciated securities)",
                "Tax-managed investment approaches",
                "Consider opportunity zone investments for capital gains"
            ]
        }
    
    # Add account-specific strategies
    for account in account_types:
        if account == "401k":
            strategies["retirement_account_strategies"]["401k"] = {
                "contributions": "Maximize pre-tax contributions to reduce taxable income",
                "investments": "Focus on high-growth, dividend-paying, or tax-inefficient investments",
                "withdrawals": "Plan for required minimum distributions (RMDs) starting at age 72"
            }
        elif account == "ira":
            strategies["retirement_account_strategies"]["traditional_ira"] = {
                "contributions": "May be tax-deductible depending on income and other retirement plans",
                "investments": "Focus on income-generating or tax-inefficient investments",
                "withdrawals": "Plan for required minimum distributions (RMDs) starting at age 72"
            }
        elif account == "roth_ira":
            strategies["retirement_account_strategies"]["roth_ira"] = {
                "contributions": "After-tax contributions with no immediate tax benefit",
                "investments": "Focus on highest growth potential investments",
                "withdrawals": "Tax-free qualified withdrawals, no RMDs during owner's lifetime"
            }
        elif account == "hsa":
            strategies["retirement_account_strategies"]["hsa"] = {
                "contributions": "Triple tax advantage: tax-deductible contributions, tax-free growth, tax-free withdrawals for qualified expenses",
                "investments": "Consider using as a retirement supplement by paying medical expenses out-of-pocket",
                "withdrawals": "Save receipts for future tax-free withdrawals"
            }
    
    return json.dumps({
        "tax_optimization_strategies": strategies,
        "disclaimer": "These strategies are for educational purposes only and do not constitute tax advice. Please consult with a tax professional for personalized guidance."
    })

def create_financial_plan(age: int, retirement_age: int = 65, current_savings: float = 0, monthly_contribution: float = 0, risk_profile: str = "moderate"):
    """
    Create a long-term financial plan focused on retirement and wealth building.
    
    Args:
        age: Current age of the user
        retirement_age: Target retirement age
        current_savings: Current retirement savings
        monthly_contribution: Monthly contribution to savings/investments
        risk_profile: Risk profile (conservative, moderate, aggressive)
    
    Returns:
        JSON string with financial plan
    """
    years_to_retirement = retirement_age - age
    
    # Estimated returns based on risk profile
    annual_returns = {
        "conservative": 0.05,  # 5%
        "moderate": 0.07,      # 7%
        "aggressive": 0.09     # 9%
    }
    
    if risk_profile not in annual_returns:
        risk_profile = "moderate"
    
    expected_return = annual_returns[risk_profile]
    
    # Calculate future value of current savings
    future_value_current_savings = current_savings * ((1 + expected_return) ** years_to_retirement)
    
    # Calculate future value of monthly contributions
    annual_contribution = monthly_contribution * 12
    future_value_contributions = annual_contribution * (((1 + expected_return) ** years_to_retirement) - 1) / expected_return
    
    # Total projected retirement savings
    total_retirement_savings = future_value_current_savings + future_value_contributions
    
    # Estimate retirement income using the 4% rule
    annual_retirement_income = total_retirement_savings * 0.04
    monthly_retirement_income = annual_retirement_income / 12
    
    # Create milestone targets
    milestones = []
    for milestone_year in range(5, years_to_retirement + 1, 5):
        milestone_savings = current_savings * ((1 + expected_return) ** milestone_year)
        milestone_contributions = annual_contribution * (((1 + expected_return) ** milestone_year) - 1) / expected_return
        milestone_total = milestone_savings + milestone_contributions
        
        milestones.append({
            "years_from_now": milestone_year,
            "age": age + milestone_year,
            "projected_savings": round(milestone_total, 2)
        })
    
    # Generate phase-based investment strategies
    investment_phases = []
    
    if years_to_retirement > 20:
        investment_phases.append({
            "phase": "Growth Phase (20+ years to retirement)",
            "allocation": {
                "stocks": 80 if risk_profile == "aggressive" else 70 if risk_profile == "moderate" else 60,
                "bonds": 10 if risk_profile == "aggressive" else 20 if risk_profile == "moderate" else 30,
                "alternatives": 10,
                "cash": 0
            },
            "focus": "Maximize growth potential",
            "strategies": [
                "Emphasize equity investments, particularly growth stocks and funds",
                "Consider international and emerging market exposure",
                "Begin building a dividend growth portfolio",
                "Minimal bond allocation focused on higher yields"
            ]
        })
    
    if 10 <= years_to_retirement <= 20:
        investment_phases.append({
            "phase": "Growth-and-Income Phase (10-20 years to retirement)",
            "allocation": {
                "stocks": 70 if risk_profile == "aggressive" else 60 if risk_profile == "moderate" else 50,
                "bonds": 20 if risk_profile == "aggressive" else 30 if risk_profile == "moderate" else 40,
                "alternatives": 10,
                "cash": 0
            },
            "focus": "Balance between growth and income",
            "strategies": [
                "Shift toward dividend-paying stocks and funds",
                "Increase bond allocation gradually",
                "Consider REITs for income and diversification",
                "Begin tax optimization strategies"
            ]
        })
    
    if 5 <= years_to_retirement < 10:
        investment_phases.append({
            "phase": "Pre-Retirement Phase (5-10 years to retirement)",
            "allocation": {
                "stocks": 60 if risk_profile == "aggressive" else 50 if risk_profile == "moderate" else 40,
                "bonds": 30 if risk_profile == "aggressive" else 40 if risk_profile == "moderate" else 50,
                "alternatives": 5,
                "cash": 5
            },
            "focus": "Capital preservation with moderate growth",
            "strategies": [
                "Reduce portfolio volatility",
                "Increase focus on income-generating investments",
                "Begin building bond ladder for retirement income",
                "Consider annuities for guaranteed income (portion of portfolio)"
            ]
        })
    
    if years_to_retirement < 5:
        investment_phases.append({
            "phase": "Retirement Transition Phase (<5 years to retirement)",
            "allocation": {
                "stocks": 50 if risk_profile == "aggressive" else 40 if risk_profile == "moderate" else 30,
                "bonds": 40 if risk_profile == "aggressive" else 50 if risk_profile == "moderate" else 60,
                "alternatives": 0,
                "cash": 10
            },
            "focus": "Capital preservation and income generation",
            "strategies": [
                "Build cash buffer for initial retirement years",
                "Finalize retirement income strategy",
                "Consider Qualified Charitable Distributions if applicable",
                "Review and optimize Social Security claiming strategy"
            ]
        })
    
    # Add retirement phase
    investment_phases.append({
        "phase": "Retirement Phase",
        "allocation": {
            "stocks": 40 if risk_profile == "aggressive" else 30 if risk_profile == "moderate" else 20,
            "bonds": 50 if risk_profile == "aggressive" else 60 if risk_profile == "moderate" else 70,
            "alternatives": 0,
            "cash": 10
        },
        "focus": "Income generation and capital preservation",
        "strategies": [
            "Implement systematic withdrawal strategy",
            "Focus on dividend and interest income",
            "Manage sequence of returns risk",
            "Optimize tax efficiency of withdrawals"
        ]
    })
    
    return json.dumps({
        "current_age": age,
        "retirement_age": retirement_age,
        "years_to_retirement": years_to_retirement,
        "current_savings": current_savings,
        "monthly_contribution": monthly_contribution,
        "risk_profile": risk_profile,
        "expected_annual_return": expected_return * 100,
        "projected_retirement_savings": round(total_retirement_savings, 2),
        "estimated_annual_retirement_income": round(annual_retirement_income, 2),
        "estimated_monthly_retirement_income": round(monthly_retirement_income, 2),
        "milestones": milestones,
        "investment_phases": investment_phases,
        "disclaimer": "This projection is for illustrative purposes only and does not guarantee future results. Actual returns will vary and may be higher or lower than the estimates provided."
    })

# Define specialized agents
portfolio_analysis_agent = Agent(
    name="Portfolio Analyzer",
    instructions="""You are a portfolio analysis specialist. Your role is to analyze investment portfolios and provide detailed insights.
    
    When analyzing a portfolio:
    1. Assess the current allocation across asset classes
    2. Evaluate the risk level and diversification
    3. Identify strengths and weaknesses in the portfolio
    4. Calculate key performance metrics
    5. Provide clear, actionable insights
    
    Be thorough, data-driven, and objective in your analysis. Use financial terminology appropriately but explain concepts clearly.
    Avoid making specific buy/sell recommendations - that's the job of the Recommendation Specialist.
    """,
    functions=[analyze_portfolio, transfer_to_market_trends, transfer_to_recommendation, transfer_to_tax_specialist, transfer_to_financial_planning]
)

market_trends_agent = Agent(
    name="Market Trends Analyst",
    instructions="""You are a market trends analyst specializing in identifying and explaining market patterns and economic indicators.
    
    Your responsibilities include:
    1. Analyzing current market conditions across different sectors
    2. Identifying emerging trends and potential opportunities
    3. Explaining economic indicators and their implications
    4. Providing context on market volatility and sentiment
    5. Offering insights on macroeconomic factors affecting investments
    
    Base your analysis on data, not speculation. Acknowledge uncertainty where appropriate.
    Avoid making specific investment recommendations - that's the job of the Recommendation Specialist.
    """,
    functions=[get_market_data, transfer_to_portfolio_analysis, transfer_to_recommendation, transfer_to_tax_specialist, transfer_to_financial_planning]
)

recommendation_agent = Agent(
    name="Investment Recommendation Specialist",
    instructions="""You are an investment recommendation specialist. Your role is to provide tailored investment suggestions based on user goals, risk tolerance, and market conditions.
    
    When making recommendations:
    1. Consider the user's risk profile, time horizon, and financial goals
    2. Suggest specific investment vehicles (stocks, ETFs, bonds, etc.) that align with their objectives
    3. Explain the rationale behind each recommendation
    4. Provide a balanced view of potential risks and rewards
    5. Consider tax implications and efficiency
    
    Always include a disclaimer that your recommendations are for educational purposes only and not financial advice.
    Emphasize long-term wealth building over short-term gains or market timing.
    """,
    functions=[get_investment_recommendations, transfer_to_portfolio_analysis, transfer_to_market_trends, transfer_to_tax_specialist, transfer_to_financial_planning]
)

tax_specialist_agent = Agent(
    name="Tax Optimization Specialist",
    instructions="""You are a tax optimization specialist focusing on investment-related tax strategies.
    
    Your responsibilities include:
    1. Suggesting tax-efficient investment approaches
    2. Explaining concepts like tax-loss harvesting, asset location, and capital gains management
    3. Discussing tax-advantaged accounts and their benefits
    4. Providing general guidance on minimizing tax impact on investments
    5. Helping with retirement account tax planning
    
    Always clarify that you're providing educational information, not personalized tax advice.
    Recommend consulting with a tax professional for specific situations.
    """,
    functions=[get_tax_optimization_strategies, transfer_to_portfolio_analysis, transfer_to_recommendation, transfer_to_market_trends, transfer_to_financial_planning]
)

financial_planning_agent = Agent(
    name="Financial Planning Specialist",
    instructions="""You are a financial planning specialist focusing on long-term wealth building and retirement planning.
    
    Your responsibilities include:
    1. Creating comprehensive financial plans with clear milestones
    2. Developing retirement savings strategies and projections
    3. Explaining concepts like compound growth, dollar-cost averaging, and the rule of 72
    4. Helping users understand how different investment vehicles fit into their long-term plans
    5. Providing guidance on generational wealth building and legacy planning
    
    Focus on practical, achievable strategies rather than get-rich-quick schemes.
    Emphasize the importance of consistency, patience, and disciplined investing.
    """,
    functions=[create_financial_plan, transfer_to_portfolio_analysis, transfer_to_recommendation, transfer_to_market_trends, transfer_to_tax_specialist]
)

# Define agent transfer functions
def transfer_to_portfolio_analysis():
    """Transfer the conversation to the Portfolio Analysis specialist."""
    return portfolio_analysis_agent

def transfer_to_market_trends():
    """Transfer the conversation to the Market Trends Analyst."""
    return market_trends_agent

def transfer_to_recommendation():
    """Transfer the conversation to the Investment Recommendation Specialist."""
    return recommendation_agent

def transfer_to_tax_specialist():
    """Transfer the conversation to the Tax Optimization Specialist."""
    return tax_specialist_agent

def transfer_to_financial_planning():
    """Transfer the conversation to the Financial Planning Specialist."""
    return financial_planning_agent

# Main Investment Planner Agent
investment_planner = Agent(
    name="Investment Planner",
    instructions="""You are an AI Investment Planner designed to help users build and manage investment portfolios for long-term wealth creation.

    Your capabilities include:
    1. Analyzing existing investment portfolios
    2. Providing insights on market trends and opportunities
    3. Making personalized investment recommendations
    4. Suggesting tax optimization strategies
    5. Creating long-term financial plans for wealth building
    
    Assess each user query and either:
    - Answer directly if the question is general
    - Transfer to a specialist agent for detailed analysis or recommendations
    
    Important guidelines:
    - Always prioritize the user's financial goals and risk tolerance
    - Focus on long-term wealth building rather than short-term trading
    - Emphasize diversification and risk management
    - Be transparent about the limitations of AI financial advice
    - Include appropriate disclaimers when making recommendations
    
    Remember that you're providing educational information, not personalized financial advice.
    """,
    functions=[
        transfer_to_portfolio_analysis,
        transfer_to_market_trends,
        transfer_to_recommendation,
        transfer_to_tax_specialist,
        transfer_to_financial_planning
    ]
)

# Main execution
if __name__ == "__main__":
    client = Swarm()
    print("Starting AI Investment Planner")
    print("How can I help you with your investment planning today?")
    
    messages = []
    agent = investment_planner
    
    while True:
        user_input = input("\033[90mUser\033[0m: ")
        messages.append({"role": "user", "content": user_input})
        
        response = client.run(agent=agent, messages=messages)
        pretty_print_messages(response.messages)
        
        messages.extend(response.messages)
        agent = response.agent
