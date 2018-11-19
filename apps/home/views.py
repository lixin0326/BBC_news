from flask import Blueprint, render_template

home = Blueprint('home', __name__)


# 　首页
@home.route('/')
def index():
    return render_template('index.html')

#   分类
@home.route('/cart')
def cart():
    return render_template('cart.html')