import dataclasses
import uuid
from dataclasses import dataclass

from injector import inject
from pkg.sqlalchemy import SQLAlchemy
from internal.model.app import App


@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self)->App:
        with self.db.auto_commit():
            app = App(name="app", account_id=uuid.uuid4(), icon="",description="app description")
            self.db.session.add(app)
        return app

    def get_app(self, app_id: uuid.UUID)->App:
        return self.db.session.query(App).get(app_id)

    def update_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "慕课聊天机器人"
        return app
    def delete_app(self, id: uuid.UUID)->None:
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)
        return app
