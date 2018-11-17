from flask_restful import Resource, reqparse

from apps.home.models import User, News
from apps.comm.result import Result


class IndexApi(Resource):
    def get(self):
        user = User.query.all()
        return 'hello flask'


# 分类的接口
class ClassifyApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=int, required=True)
        self.parser.add_argument('page', type=int, default=1)
        self.parser.add_argument('size', type=int, default=10)

    def get(self):
        args = self.parser.parse_args()
        c_id = args.get('c_id')
        news_list_count = News.query.filter(News.c_id == c_id).count()
        news_list = News.query.filter(News.c_id == c_id).limit(5).offset(0).all()
        data = {
            'news': {
                'news_list_count': news_list_count,
                'news_list': news_list,
            },

        }

        return Result.get_success_result(data)
