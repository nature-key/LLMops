from datetime import datetime
from http.client import responses

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



responses = llm.stream(prompt.invoke({"query": "你好，你知道agent程序员吗"}))
for response in responses:
    print(response.content,flush=True,end="")
