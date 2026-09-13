import os
import sys

from flask_migrate import Migrate
from injector import Injector

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import Config
from app.http.module import ExtensionModule
from internal.router import Router
from internal.server.http import Http
from pkg.sqlalchemy import SQLAlchemy
import dotenv

dotenv.load_dotenv(encoding='utf-8')
config = Config()
injector = Injector([ExtensionModule])
app = Http(__name__, config=config,migrate=injector.get(Migrate),
           db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == '__main__':
    app.run()
