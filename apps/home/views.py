from flask import Blueprint, render_template

<<<<<<< HEAD
home = Blueprint('home', __name__, template_folder='templates')
=======
from apps.home.models import News, Classify

home = Blueprint('home', __name__)
import math
>>>>>>> origin/wuhengxin


# 　首页
@home.route('/')
def index():
    return render_template('index.html')


#   分类页面
@home.route('/cart/<c_id>/<page>')
def cart(c_id, page):
    news_list_count = Classify.query.filter(Classify.c_id == c_id).all()
    news_count = News.query.filter(News.classify_id == c_id).count()
    # news_count = News.query.filter(News.classify_id == c_id).all().count()
    max_page = math.ceil(news_count / 6)
    cla_name = []
    for news_cla in news_list_count:
        c_name = news_cla.c_name
        cla_name.append(c_name)
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
    return render_template('business.html',
                           news=news,
                           cla_name=cla_name,
                           page=page,
                           next_page=int(page) + 1,
                           max_page=int(max_page) + 1)


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
    return render_template('detail.html', news=news)
