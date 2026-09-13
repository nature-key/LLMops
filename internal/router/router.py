from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler

@inject
@dataclass
class Router:
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        bp = Blueprint('llmops', __name__, url_prefix='')
        app.add_url_rule("/ping", view_func=self.app_handler.ping)
        app.add_url_rule("/chat/completion",methods=["POST"], view_func=self.app_handler.completion)
        app.add_url_rule("/app",methods=["POST"], view_func=self.app_handler.create_app)
        app.add_url_rule("/app/<uuid:id>",methods=["GET"], view_func=self.app_handler.get)
        app.add_url_rule("/app/<uuid:id>",methods=["POST"], view_func=self.app_handler.update)
        app.add_url_rule("/app/<uuid:id>",methods=["DELETE"], view_func=self.app_handler.delete)
        app.register_blueprint(bp)
