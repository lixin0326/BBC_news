from flask import Flask

from apps.db_ext import init_ext
from apps.urls import init_api


def create_app():
    app = Flask(__name__)

    app.debug = True  # 注意产品上线的时候要管了

    init_api(app)  # 路由系统　拓展程序

    init_ext(app)  # 数据库相关 拓展程序

    return app
