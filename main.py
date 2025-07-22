from agents import Runner, set_tracing_disabled
from my_agent.math_agent import math_agent

set_tracing_disabled(True)

user_input = input("Enter a math question: ")

res = Runner.run_sync(starting_agent=math_agent,input=user_input)

print(res.final_output)