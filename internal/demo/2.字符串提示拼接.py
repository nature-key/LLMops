

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

prompt = (PromptTemplate.from_template("请讲关于{subject}的冷笑话")
          +",让我开心一下"+
          "\n使用{language}语言")


print(prompt)
print('*'*50)
print(prompt.format(subject="动物", language="中文"))
print(prompt.invoke({"subject": "动物", "language": "中文"}))
print(prompt.invoke({"subject": "动物", "language": "中文"}).to_string())



system_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的ai助手,我叫{username}"),
])


human_prompt = ChatPromptTemplate.from_messages([
    ("human", "{query}"),
])

prompt = system_prompt + human_prompt

print(prompt)
print(prompt.format(username="张三", query="你好"))
