from flask import render_template, Blueprint
from flask_login import login_required

account = Blueprint('account', __name__)


@account.route('/account/points/')
@login_required
def _points():
    return render_template("account/points.html")


@account.route('/account/')
@login_required
def _account():
    return render_template("account/account.html")


@account.route('/account/settings/')
@login_required
def _settings():
    return render_template("account/settings.html")
