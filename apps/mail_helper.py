###############邮箱激活#####################
from threading import Thread

from flask import current_app, render_template
from flask_mail import Mail, Message


def init_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.163.com'
    # 邮箱用户
    app.config['MAIL_USERNAME'] = 'L15737628530@163.com'
    # 用户密码
    app.config['MAIL_PASSWORD'] = 'lixin1997'




def async_send_mail(app, msg):
    # 邮件发送需要在程序上下文中进行，
    # 新的线程中没有上下文，需要手动创建
    with app.app_context():
        # 创建Mail对象
        mail = Mail()
        mail.send(msg)


def send_mail(subject, to, templates, **kwargs):
    # 从代理中获取代理的原始对象
    app = current_app._get_current_object()
    # 创建用于发送的邮件消息对象
    msg = Message(subject=subject, recipients=[to],
                  sender=app.config['MAIL_USERNAME'])
    # 设置内容
    msg.html = render_template(templates, **kwargs)
    # 发送邮件
    # mail.send(msg)
    thr = Thread(target=async_send_mail, args=[app, msg])
    thr.start()
    return '邮件已发送'


'''
配置邮箱服务器
'''

'''
封装函数发送邮件
'''
