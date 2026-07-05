from langchain.agents import create_agent

from app.ai.gemini import llm
from app.ai.prompt_loader import PromptLoader
from app.tools.weather_tool import get_weather

system_prompt = PromptLoader.load("weather_agent.txt")

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt=system_prompt
)