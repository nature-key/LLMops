import dotenv
from langchain_core import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI


dotenv.load_dotenv()
prompt = ChatPromptTemplate.from_template("""
请根据用户提问，返回用户提问的内容，可以参考上下文
<context>
{context}
</context>
用户提问:{query}
""")


def message(query: str) -> str:
    print("检索上下文中")
    return "我是程序员"


llm = ChatOpenAI(model="qwen3.7-plus")

parser = StrOutputParser()

chain = RunnableParallel(
    context=message,
    query=RunnablePassthrough(),
) | prompt | llm | parser


context=chain.invoke("你是谁")
print(context)


