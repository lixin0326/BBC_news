from flask_restful import Resource

from apps.home.models import User


class IndexApi(Resource):
    def get(self):
        user = User.query.all()
        return 'hello flask'
