from flask import Blueprint, session

from apps.home.models import User

personal = Blueprint('personal', __name__)


@personal.route('/PersonCenter/')
def PersonCenter():
    username = session['username']
    user = User.query.filter_by(username=username).first()
    if user:
        password = user.password

        email = user.email

        return f'{password} {email}'
    else:
        return '用户信息查询失败!'
