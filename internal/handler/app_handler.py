import os
import uuid
from dataclasses import dataclass

from injector import inject
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI

from internal.exception import FailException
from internal.schedule.app_schema import CompletionReq
from internal.service.app_service import AppService
from pkg import success_json, success_message


@inject
@dataclass
class AppHandler:
    app_service: AppService

    def completion(self):
        """聊天机器人"""
        req = CompletionReq()
        if not req.validate():
            return req.errors
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(model="qwen3.7-plus")
        parser = StrOutputParser()
        output = prompt | llm | parser
        content = output.invoke({"query": req.query.data})
        # completion = client.chat.completions.create(
        #     # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        #     model="qwen-plus",
        #     messages=[
        #         {"role": "system", "content": "你是一个专业的ai助手"},
        #         {"role": "user", "content": req.query.data},
        #     ]
        # )
        # content = completion.choices[0].message.content

        return success_json({"content": content})

    def create_app(self):
        """创建应用"""
        app = self.app_service.create_app()
        return success_json(f"创建应用成功，应用ID：{app.id}")

    def get(self, id: uuid.UUID):
        """获取应用"""
        app = self.app_service.get_app(id)
        if not app:
            raise FailException("应用不存在")
        return success_message(f"应用已经成功获取，名字是{app.name}")

    def update(self, id: uuid.UUID):
        """更新应用"""
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功更新，名字是{app.name}")

    def delete(self, id: uuid.UUID):
        """删除应用"""
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，名字是{app.id}")

    def ping(self):
        # return {"ping": "pong"}
        raise FailException("数据没有找到")
