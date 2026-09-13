

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI


dotenv.load_dotenv()




joke_prompt=ChatPromptTemplate.from_template("你是一个{query}，因此你喜欢的笑话是：")
pom_prompt=ChatPromptTemplate.from_template("你是一个{query}，因此你喜欢的食物是：")

llm =ChatOpenAI(model="qwen3.7-plus")


outPutParser = StrOutputParser()


joke_chain = joke_prompt | llm | outPutParser
pom_chain = pom_prompt | llm | outPutParser


res = RunnableParallel({
    "query": joke_chain,
    "pom": pom_chain,
})

print(res.invoke({"query": "程序员"}))




