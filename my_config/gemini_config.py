from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel

key=config("GEMINI_API_KEY")
base_url=config("BASE_URL")

client = AsyncOpenAI(api_key=key,base_url=base_url)

MODEL = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)