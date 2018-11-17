from flask_restful import Api

from apps.home.apis import IndexApi
from apps.user.api import AccountApi

api = Api(prefix='/api/v1/')  # 前缀


def init_api(app):
    api.init_app(app)


# 注册路由系统
api.add_resource(IndexApi, 'home/')
api.add_resource(AccountApi, 'account/')