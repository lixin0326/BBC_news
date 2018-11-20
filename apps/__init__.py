from flask import Flask
from apps.account.views import account
from apps.db_ext import init_ext
from apps.home.views import home



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456'  # 用于保存session的

    app.debug = True  # 注意产品上线的时候要管了

    register_blue(app)  # 注册蓝图对象

    init_ext(app)  # 数据库相关 拓展程序

    # init_mail(app)  # 邮箱激活



    return app


# 注册蓝图对象
def register_blue(app):
    app.register_blueprint(home)
    app.register_blueprint(account)
