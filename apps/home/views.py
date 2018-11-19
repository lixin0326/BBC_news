from flask import Blueprint, render_template

home = Blueprint('home', __name__)


# 　首页
@home.route('/')
def index():
    return render_template('index.html')
