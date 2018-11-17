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


