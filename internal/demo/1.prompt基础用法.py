from datetime import datetime

from langchain_core.messages import AIMessage
from langchain_core.prompts import (
    PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
)


prompt = PromptTemplate.from_template("请将一个关于{subject}的冷笑话")
print(prompt)
print(prompt.format(subject="动物"))

print('*'*50)
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的ai助手,当前时间：{now}"),
    MessagesPlaceholder("chat_history"),
    HumanMessagePromptTemplate.from_template("请讲关于{subject}的冷笑话")
]).partial(now=datetime.now())
char_prompt_value=chat_prompt.invoke({
    "chat_history": [
        ("user", "你好"),
        AIMessage(content="你好，我是专业的ai助手")
    ],
    "subject": "动物"
})
print(chat_prompt)
print(char_prompt_value)
print(char_prompt_value.to_messages())
print(char_prompt_value.to_string())
