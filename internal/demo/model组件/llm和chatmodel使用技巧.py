from datetime import datetime

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

from langchain_openai import ChatOpenAI

import dotenv

from pkg import fail_message

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的ai助手{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

print(prompt.invoke({"query": "你好，你知道程序员，35岁被裁危机吗"}).to_string())
# llm = ChatOpenAI(model="qwen3.7-plus")
# ai_message = llm.invoke(prompt.invoke({"query": "你好，你知道程序员，35岁被裁危机吗"}))
#
# print(ai_message.type)
# print('-----------------')
# print(ai_message.content)
# print('-----------------')
# print(ai_message.response_metadata)