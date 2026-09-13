from datetime import datetime

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

from langchain_openai import ChatOpenAI

import dotenv

from internal.demo.model组件.llm和chatmodel使用技巧 import ai_message
from pkg import fail_message

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的ai助手{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

llm = ChatOpenAI(model="qwen3.7-plus")

ai_message=llm.batch([
    prompt.invoke({"query": "你好，你知道程序员，35岁被裁危机吗"}),
    prompt.invoke({"query": "你好，35岁被裁危机如何破解"}),
])

for message in ai_message:
    print('-----------------')
    print(message.content)
    print('-----------------')


