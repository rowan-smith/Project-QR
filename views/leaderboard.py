from flask import render_template, Blueprint, session
from flask_login import login_required, current_user

# from app.models.User import User
from models import UserModel

leaderboard = Blueprint('leaderboard', __name__)


@leaderboard.route('/leaderboard/')
@login_required
def _points():
    session['points'] = UserModel.query.filter_by(name=session['name']).first().points
    return render_template('leaderboard/leaderboard.html', session=session, users=UserModel.query.order_by(UserModel.points.desc()).all())
