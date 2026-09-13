import dotenv
from langchain_core.output_parsers import StrOutputParser

dotenv.load_dotenv()


from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


prompt = ChatPromptTemplate.from_template("{query}")

llm = ChatOpenAI(model="qwen3.7-plus")

parser = StrOutputParser()

response = llm.invoke(prompt.invoke({"query": "你好，你知道程序员，35岁被裁危机吗"}))
print(parser.invoke(response))







