from flask_restful import Resource,reqparse

from apps.comm.result import Result
from apps.home.models import User,News


class IndexApi(Resource):
    def get(self):
        user = User.query.all()
        return 'hello flask'


