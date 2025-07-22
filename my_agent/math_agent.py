from agents import Agent
from my_config.gemini_config import MODEL
from my_tool.math_tool import add

math_agent = Agent(name="Math Agent",instructions="I can only do addition (+) questions. ",model=MODEL,tools=[add])