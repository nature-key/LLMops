from datetime import datetime

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate;
from langchain_openai import ChatOpenAI
import dotenv


dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant{now}"),
    ("human", "{input}"),
]).partial(now=datetime.now)

llm = ChatOpenAI(model="qwen3.7-plus")

# response=llm.invoke(prompt.invoke({"input": "你好"}))
#
# print(response.content)

# ai_message=llm.batch([
#     prompt.invoke({"input": "你好"}),
#     prompt.invoke({"input": "你好"}),
# ])
#
# for message in ai_message:
#     print(message.content)

result =llm.stream(prompt.invoke({"input": "西安，37岁程序员转AI agent开发，可以工作吗"}))

for chunk in result:
    print(chunk.content, flush=True, end="")



