from flask import render_template, Blueprint, session
from flask_login import login_required, current_user

# from app.models.User import User
from models import UserModel

account = Blueprint('account', __name__)


@account.route('/points/')
@login_required
def _points():
    return "<h1>Account Points</h1>"


@account.route('/account/')
@login_required
def _account():
    return "<h1>Account</h1>"


@account.route('/settings/')
@login_required
def _settings():
    return "<h1>Account Settings</h1>"
