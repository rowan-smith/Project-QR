from flask import render_template, Blueprint, session
from flask_login import login_required, current_user

# from app.models.User import User
from models import UserModel

account = Blueprint('account', __name__)


@account.route('/points')
@login_required
def _points():
    return render_template("account/account.html")


@account.route('/account')
@login_required
def _account():
    session['points'] = UserModel.query.filter_by(name=session['name']).first().points
    return render_template('account/account.html', session=session, users=UserModel.query.order_by(UserModel.points.desc()).all())


@account.route('/settings')
@login_required
def _settings():
    # TODO create a settings page
    # user = User.query.get(current_user.id)
    # print(user)
    return render_template('account/account.html')
