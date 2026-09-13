


import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompts = PromptTemplate.from_template("{query}")

llm = ChatOpenAI(model="qwen3.7-plus")

outputParser = StrOutputParser()


response = prompts|llm|outputParser

print(response.invoke({"query": "你好"}))






