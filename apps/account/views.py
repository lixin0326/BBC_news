from flask import Blueprint

account = Blueprint('account', __name__)


@account.route('/account')
def login():
    pass
