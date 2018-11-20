from flask import Blueprint, render_template

from apps.home.models import News, Classify

import math

home = Blueprint('home', __name__, template_folder='templates')


# 　首页
@home.route('/')
def index():
    categorys = Classify.query.filter().all()
    banners_list = News.query.filter().limit(4).all()
    news_left = News.query.filter().limit(3).all()
    news_right = News.query.filter().limit(3).all()
    news = News.query.filter().limit(4).offset(0).all()
    hot_news = News.query.filter().limit(6).all()
    return render_template('index.html', categorys=categorys, banners_list=banners_list, news_left=news_left,
                           news_right=news_right, news=news, hot_news=hot_news)


#   分类页面
@home.route('/cart/<c_id>/<page>')
def cart(c_id, page):
    news_classify = Classify.query.filter(Classify.c_id == c_id).all()[0]
    print(news_classify.c_name)
    news_list = News.query.filter(News.classify_id == c_id).limit(6).offset((int(page) - 1) * 6).all()
    news = []
    for new in news_list:
        new_dict = dict(
            new_id=new.new_id,
            image_url=new.image_url,
            title=new.title,
            content=new.content,
            news_date=new.news_date,
            view_count=new.view_count,
            is_hot=new.is_hot,
            classify_id=new.classify_id,
        )
        news.append(new_dict)
    return render_template('cart.html',
                           news=news,
                           cla_name=news_classify.c_name,
                           page=page,
                           )


#   详情页面
@home.route('/detail/<new_id>')
def detail(new_id):
    news_list = News.query.filter(News.new_id == new_id).offset(0).all()
    news = []
    for new in news_list:
        new_dict = dict(
            new_id=new.new_id,
            image_url=new.image_url,
            title=new.title,
            content=new.content,
            news_date=new.news_date,
            view_count=new.view_count,
            is_hot=new.is_hot,
            classify_id=new.classify_id,
        )
        news.append(new_dict)
    return render_template('home/detail.html', news=news)
