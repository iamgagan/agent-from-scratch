from dotenv import load_dotenv
_ = load_dotenv()

import json
import time
from investment_planner import (
    Swarm, 
    investment_planner,
    portfolio_analysis_agent,
    market_trends_agent, 
    recommendation_agent,
    tax_specialist_agent,
    financial_planning_agent,
    analyze_portfolio,
    get_market_data,
    get_investment_recommendations,
    get_tax_optimization_strategies,
    create_financial_plan
)

def print_header(title):
    """Print a formatted header for demonstrations"""
    print("\n" + "=" * 80)
    print(f"{title}".center(80))
    print("=" * 80 + "\n")

def print_json(json_str):
    """Pretty print JSON data"""
    try:
        data = json.loads(json_str)
        print(json.dumps(data, indent=2))
    except:
        print(json_str)

def run_demo(agent, prompt, show_functions=False):
    """Run a demonstration with the specified agent and prompt"""
    client = Swarm()
    messages = [{"role": "user", "content": prompt}]
    
    print(f"\033[90mUser\033[0m: {prompt}")
    
    # If show_functions is True, directly call and display function outputs
    if show_functions:
        if agent == portfolio_analysis_agent:
            print("\n\033[94mFunction Output (analyze_portfolio)\033[0m:")
            result = analyze_portfolio()
            print_json(result)
            print("\n")
        elif agent == market_trends_agent:
            print("\n\033[94mFunction Output (get_market_data)\033[0m:")
            result = get_market_data()
            print_json(result)
            print("\n")
        elif agent == recommendation_agent:
            print("\n\033[94mFunction Output (get_investment_recommendations)\033[0m:")
            result = get_investment_recommendations()
            print_json(result)
            print("\n")
        elif agent == tax_specialist_agent:
            print("\n\033[94mFunction Output (get_tax_optimization_strategies)\033[0m:")
            result = get_tax_optimization_strategies()
            print_json(result)
            print("\n")
        elif agent == financial_planning_agent:
            print("\n\033[94mFunction Output (create_financial_plan)\033[0m:")
            result = create_financial_plan(35, 65, 50000, 1000, "moderate")
            print_json(result)
            print("\n")
    
    # Run the agent conversation
    response = client.run(agent=agent, messages=messages)
    
    # Display the response
    for message in response.messages:
        if message["role"] == "assistant" and message.get("content"):
            print(f"\033[94m{message['sender']}\033[0m: {message['content']}")
        elif message["role"] == "tool":
            tool_name = message.get("tool_name", "")
            print(f"\033[93mTool ({tool_name})\033[0m: {message['content'][:100]}...")
    
    # If the agent transferred to another specialist, mention it
    if response.agent and response.agent.name != agent.name:
        print(f"\n\033[95mTransferred to: {response.agent.name}\033[0m\n")
    
    return response

def demo_portfolio_analysis():
    print_header("Portfolio Analysis Demonstration")
    prompt = """
    I'd like to analyze my current investment portfolio. Here's what I have:
    - 10 shares of Apple (AAPL) bought at $150
    - 5 shares of Microsoft (MSFT) bought at $250
    - 15 shares of SPY ETF bought at $400
    - $10,000 in Treasury Bonds with 3.5% yield
    - $15,000 in cash
    
    Can you analyze my portfolio and tell me if it's well-balanced?
    """
    run_demo(portfolio_analysis_agent, prompt, show_functions=True)

def demo_market_trends():
    print_header("Market Trends Analysis Demonstration")
    prompt = """
    What are the current trends in the technology sector? 
    I'm particularly interested in understanding if now is a good time to invest in tech stocks.
    Also, how are interest rates affecting the overall market?
    """
    run_demo(market_trends_agent, prompt, show_functions=True)

def demo_investment_recommendations():
    print_header("Investment Recommendations Demonstration")
    prompt = """
    I'm 35 years old with a moderate risk tolerance and looking to build wealth for retirement in 30 years.
    I'm also interested in creating some passive income streams along the way.
    What investment strategy would you recommend? Can you suggest specific ETFs or stocks I should consider?
    """
    run_demo(recommendation_agent, prompt, show_functions=True)

def demo_tax_optimization():
    print_header("Tax Optimization Demonstration")
    prompt = """
    I'm in a high-income bracket and currently have investments in a 401(k), Roth IRA, and a taxable brokerage account.
    What tax optimization strategies would you recommend for my investments? 
    How should I allocate different types of investments across these accounts to minimize taxes?
    """
    run_demo(tax_specialist_agent, prompt, show_functions=True)

def demo_financial_planning():
    print_header("Financial Planning Demonstration")
    prompt = """
    I'm 35 years old and want to retire by 65. I currently have $50,000 saved and can contribute $1,000 monthly.
    My risk tolerance is moderate. Can you create a financial plan that will help me build generational wealth?
    What milestones should I aim for, and how should my investment strategy evolve over time?
    """
    run_demo(financial_planning_agent, prompt, show_functions=True)

def demo_multi_agent():
    print_header("Multi-Agent System Demonstration")
    prompt = """
    I'd like to build generational wealth through smart investing. I'm 40 years old with $100,000 to invest.
    Can you analyze the current market conditions, recommend a diversified portfolio, suggest tax optimization
    strategies, and create a long-term financial plan that will help me achieve my goals?
    """
    
    print(f"\033[90mUser\033[0m: {prompt}")
    print("\n\033[94mStarting with main Investment Planner agent\033[0m\n")
    
    client = Swarm()
    messages = [{"role": "user", "content": prompt}]
    agent = investment_planner
    
    # Run a few turns to demonstrate agent transfers
    for _ in range(3):
        response = client.run(agent=agent, messages=messages, max_turns=1)
        
        for message in response.messages:
            if message["role"] == "assistant" and message.get("content"):
                print(f"\033[94m{message['sender']}\033[0m: {message['content']}")
            elif message["role"] == "tool":
                tool_name = message.get("tool_name", "")
                print(f"\033[93mTool ({tool_name})\033[0m: {message['content'][:100]}...")
        
        messages.extend(response.messages)
        
        if response.agent and response.agent.name != agent.name:
            print(f"\n\033[95mTransferred to: {response.agent.name}\033[0m\n")
            agent = response.agent
            time.sleep(1)  # Pause to make the transfer more visible

def interactive_mode():
    print_header("Interactive Investment Planner")
    print("You can now interact directly with the AI Investment Planner.")
    print("Type 'exit' to return to the main menu.\n")
    
    client = Swarm()
    messages = []
    agent = investment_planner
    
    while True:
        user_input = input("\033[90mUser\033[0m: ")
        if user_input.lower() == 'exit':
            break
            
        messages.append({"role": "user", "content": user_input})
        response = client.run(agent=agent, messages=messages)
        
        for message in response.messages:
            if message["role"] == "assistant" and message.get("content"):
                print(f"\033[94m{message['sender']}\033[0m: {message['content']}")
            elif message["role"] == "tool":
                tool_name = message.get("tool_name", "")
                print(f"\033[93mTool ({tool_name})\033[0m: {message['content'][:100]}...")
        
        messages.extend(response.messages)
        
        if response.agent and response.agent.name != agent.name:
            print(f"\n\033[95mTransferred to: {response.agent.name}\033[0m\n")
            agent = response.agent

def main_menu():
    while True:
        print_header("AI Investment Planner Demo")
        print("1. Portfolio Analysis Demonstration")
        print("2. Market Trends Analysis Demonstration")
        print("3. Investment Recommendations Demonstration")
        print("4. Tax Optimization Demonstration")
        print("5. Financial Planning Demonstration")
        print("6. Multi-Agent System Demonstration")
        print("7. Interactive Mode")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-7): ")
        
        if choice == '1':
            demo_portfolio_analysis()
        elif choice == '2':
            demo_market_trends()
        elif choice == '3':
            demo_investment_recommendations()
        elif choice == '4':
            demo_tax_optimization()
        elif choice == '5':
            demo_financial_planning()
        elif choice == '6':
            demo_multi_agent()
        elif choice == '7':
            interactive_mode()
        elif choice == '0':
            print("\nThank you for using the AI Investment Planner Demo!")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    print_header("AI Investment Planner Demo")
    print("""
    Welcome to the AI Investment Planner Demo!
    
    This demonstration showcases an AI-powered investment planning system
    that can help users analyze portfolios, understand market trends,
    receive investment recommendations, optimize tax strategies,
    and create long-term financial plans for building generational wealth.
    
    The system uses a multi-agent architecture with specialized agents for:
    - Portfolio Analysis
    - Market Trends Analysis
    - Investment Recommendations
    - Tax Optimization
    - Financial Planning
    
    Note: All financial data in this demo is simulated for demonstration purposes.
    In a production environment, this would connect to real financial APIs and data sources.
    """)
    
    input("Press Enter to continue to the main menu...")
    main_menu()
