import datetime
import uuid
from functools import wraps
from flask import Blueprint, request, render_template, session, redirect, url_for
from flask_mail import Message

from apps.db_ext import db, mail
from apps.home.models import User

account = Blueprint('account', __name__)


# 登录装饰器
def login_required(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        if session.get('username'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('account.login', next=request.url))

    return __wrapper


@account.route('/', methods=['GET', 'POST'])
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
            session['username'] = username

            return redirect('/')
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
            # token = str(uuid.uuid4())
            active_url = 'http://127.0.0.1:8000/active_user/?username=%s' % username

            html = render_template('user_active.html', username=username, active_url=active_url)
            msg = Message(subject='激活账号邮件', body='全球最帅男子', sender='L15737628530@163.com',
                          recipients=[email, ], html=html)
            mail.send(msg)

            return '激活邮件已发送!'

        except Exception as e:
            print(e)
        return redirect('/')


@account.route('/login_out/')
def login_out():
    session.clear()
    return redirect('/')


@account.route('/active_user/')
def ActiveUser():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()  # 注意这里边的first()
    if user:
        user.is_active = 1
        db.session.commit()

        return '激活成功!'
    else:
        return '激活失败!'
