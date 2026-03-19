"""
LangChain + NVIDIA Kimi K2.5 AI Agent with demo tools + web search.
Run: python agent.py
"""
import os
import re
from datetime import datetime

from dotenv import load_dotenv

# Load .env from current directory
load_dotenv()

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city. Use this when the user asks about weather."""
    # Mock weather for demo - replace with real API (e.g. OpenWeatherMap) later
    return f"Weather in {city}: 72°F, sunny"


@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression. Use for calculations like '2+3*4' or '100/5'."""
    expression = expression.strip()
    if not re.match(r"^[\d\s+\-*/().]+$", expression):
        return "Error: Only numbers and math operators + - * / ( ) allowed"
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def current_time() -> str:
    """Get the current date and time. Use when the user asks what time or date it is."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Web search tool (real - uses DuckDuckGo, no API key needed)
search_web = DuckDuckGoSearchRun()


def main():
    api_key = os.environ.get("NVIDIA_API_KEY")
    if not api_key:
        print("Error: Set NVIDIA_API_KEY in .env or environment")
        return

    llm = ChatNVIDIA(
        model="moonshotai/kimi-k2.5",
        api_key=api_key,
        temperature=0.6,
    )

    tools = [get_weather, calculator, current_time, search_web]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful assistant. Use the available tools when needed. Use search_web for current events, news, or anything you need to look up online.",
    )

    print("LangChain + Kimi K2.5 Agent (type 'quit' or 'exit' to stop)\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        try:
            result = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )
            messages = result.get("messages", [])
            last_msg = messages[-1] if messages else None
            output = (
                getattr(last_msg, "content", str(last_msg))
                if last_msg
                else "No response"
            )
            if isinstance(output, list):
                output = output[0].get("text", str(output)) if output else str(output)
            print(f"\nAgent: {output}\n")
        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()
