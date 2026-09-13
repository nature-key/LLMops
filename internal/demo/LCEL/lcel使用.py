# from typing import Any
#
# import dotenv
#
# dotenv.load_dotenv()
#
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import OpenAI, ChatOpenAI
#
# prompts = PromptTemplate.from_template("{query}")
#
# chat = ChatOpenAI(model="qwen3.7-plus")
# outputParser = StrOutputParser()
#
# inputList = [prompts, chat, outputParser]
#
#
# class Chain:
#     steps: list = [];
#
#     def __init__(self, steps: list):
#         self.steps = steps
#
#     def invoke(self, intput: Any) -> Any:
#         for step in self.steps:
#             input = step.invoke(intput)
#             print("步骤:", step)
#             print("输入:", input)
#             print("--"*20)
#         return input
#
# chain = Chain(list(inputList))
#
# print(chain.invoke("你好"))
