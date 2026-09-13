import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from internal.model import App
from config import Config
from internal.exception import FailException, CustomException
from internal.router import Router
from pkg import Response, json, HttpCode


class Http(Flask):

    def __init__(self, *args, config: Config,migrate:Migrate,db: SQLAlchemy, router: Router, **kwargs):
        super(Http, self).__init__(*args, **kwargs)
        # 初始化应用配置对象
        self.config.from_object(config)
        # 初始化数据库
        db.init_app(self)
        migrate.init_app(self,db,directory="internal/migration")
        # with self.app_context():
        #     _=App()
        #     db.create_all()
        self.register_error_handler(Exception, self._register_error_handler)
        # 注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data,
            ))
        print(self.debug)
        print('*'*20)
        print(os.getenv("FLASK_ENV"))
        if os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={},
            ))
