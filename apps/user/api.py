from flask_mail import Message
from flask_restful import Resource, reqparse
from sqlalchemy import or_
from flask import render_template

# 回调函数
from apps.db_ext import lm, db, mail
from apps.home.models import User


@lm.user_loader
def login_user(uid):
    return User.query.get(uid)


# 一个接口实现四个方法登录注册修改删除,当然在实际开发过程中也可以定义四个接口
class AccountApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True)
        self.parser.add_argument('password', type=str, required=True)
        self.parser.add_argument('email', type=str, required=True)

    def get(self):
        # 登录
        pass

    def post(self):
        # 注册
        args = self.parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        email = args.get('email')
        # 判断邮箱或者用户名是否已经被注册
        if not User.query.filter(or_(User.username == username, User.email == email)).all():
            user = User()
            user.username = username
            user.password = password
            user.email = email
            db.session.add(user)
            # db.session.commit() 在ext中设置了自动提交
            # 邮箱激活  页面
            html = render_template('mail.html')
            msg = Message(subject='激活账号邮件', body='全球最帅男子', sender='L15737628530@163.com',
                          recipients=['L18736262608@163.com', ])
            mail.send(msg)
            return 'success'
        else:
            return '用户名或邮箱已经存在,请重新注册!'

    def put(self):
        # 修改
        pass

    def delete(self):
        # 删除
        pass
