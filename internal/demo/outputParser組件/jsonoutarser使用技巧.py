import dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic.v1 import BaseModel, Field

dotenv.load_dotenv()


class Joke(BaseModel):
    joke: str = Field(description="一个笑话")
    punchline: str = Field(description="这个冷笑话的笑点")


parser = JsonOutputParser(pydantic_object=Joke)

prompt = (ChatPromptTemplate.from_template("请根据用户的提问进行回答\n {format_instructions} \n {query}")
          .partial(format_instructions=parser.get_format_instructions()))


llm = ChatOpenAI(model="qwen3.7-plus")

response = llm.invoke(prompt.invoke({"query": "讲一个冷笑话"}))
print(parser.invoke(response))
