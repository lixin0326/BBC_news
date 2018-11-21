from flask import Blueprint, render_template
from apps.home.models import News, Classify

from db_ext import db

home = Blueprint('home', __name__, template_folder='templates')


# 　首页
@home.route('/')
def index():
    categorys = Classify.query.filter().all()
    banners_list = News.query.filter().limit(4).all()
    news_left = News.query.filter().limit(3).offset(41).all()
    news_right = News.query.filter().limit(3).offset(59).all()
    news = News.query.filter().all()
    hot_news = News.query.filter_by(is_hot=1).limit(6).all()
    return render_template('index.html', categorys=categorys, banners_list=banners_list, news_left=news_left,
                           news_right=news_right, news=news, hot_news=hot_news, dets=news)


#   分类页面
@home.route('/cart/<int:c_id>/<int:page>')
def cart(c_id, page):
    if not page:
        page = 1
    categorys = Classify.query.filter().all()
    news_classify = Classify.query.filter(Classify.c_id == c_id).all()[0]
    news = News.query.filter_by(classify_id=c_id).paginate(page=page, per_page=6)
    news_classify.view_count += 1
    db.session.commit()
    return render_template('cart.html', news=news.items, classify=news_classify,
                           dets=news, categorys=categorys)


#   详情页面
@home.route('/detail/<new_id>')
def detail(new_id):
    categorys = Classify.query.filter().all()
    new = News.query.filter(News.new_id == new_id).all()[0]
    new.view_count += 1
    db.session.commit()
    return render_template('home/detail.html', new=new, categorys=categorys)
