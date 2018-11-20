import datetime
from functools import wraps
from flask import Blueprint, request, render_template, session, redirect, url_for
from sqlalchemy import and_, or_
from apps.db_ext import db
from apps.home.models import User
from mail_helper import send_mail

account = Blueprint('account', __name__)


# 登录校验
def valid_login(username, password):
    user = User.query.filter(and_(User.username == username, User.password == password))
    if user:
        return True
    else:
        return False


# 注册校验
def vlaid_register(username, email):
    user = User.query.filter(or_(User.username == username, User.email == email))
    if user:
        return False
    else:
        return True


# 登录装饰器
def login_required(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        if session.get('username'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('account.login', next=request.url))

    return __wrapper


@account.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    else:

        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            if user.is_active == 0:
                return "该用户未被激活!"

            return render_template('index.html', user=user)
        else:
            return '用户名或密码错误!'


@account.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('home/registration.html')
    else:
        username = request.form['username']
        password = request.form['password']
        confirm_pwd = request.form['confirm_pwd']
        if password != confirm_pwd:
            return '两次密码不一致!'
        email = request.form['email']
        create_date = datetime.datetime.now()
        user = User.query.filter_by(username=username).first()
        if user:
            return "该用户已被注册!"
        user = User(username=username,
                    password=password,
                    email=email,
                    create_date=create_date)
        db.session.add(user)

        try:
            send_mail(user,
                      'L18736262608@163.com',
                      'user_active.html',
                      username=user.username)
            return '邮件已发送!'
        except Exception as e:
            print(e)
        return redirect('/')


@account.route('/login_out/')
def login_out():
    session.clear()
    return render_template('index.html')
