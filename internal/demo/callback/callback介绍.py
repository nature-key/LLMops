from typing import Any
from uuid import UUID

import dotenv
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from langchain_core.outputs import GenerationChunk, ChatGenerationChunk
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

class LlmBack(BaseCallbackHandler):

    def on_llm_start(
        self,
        serialized: dict[str, Any],
        prompts: list[str],
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        tags: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Any:
        print("on_llm_start")
        print(serialized)
        print(prompts)

    def on_llm_new_token(
        self,
        token: str | list[str | dict[str, Any]],
        *,
        chunk: GenerationChunk | ChatGenerationChunk | None = None,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        tags: list[str] | None = None,
        **kwargs: Any,
    ) -> Any:
        print("on_llm_new_token")
        print(token)
        # print(chunk)

prompts = ChatPromptTemplate.from_template("{query}")

llm = ChatOpenAI(model="qwen3.7-plus")

parser = StrOutputParser();

chain = RunnableParallel({
    "query": RunnablePassthrough(),
}) | prompts | llm | parser

context = chain.stream("你是谁", config={"callbacks": [LlmBack(), StdOutCallbackHandler()]})


for r in context:
    pass
