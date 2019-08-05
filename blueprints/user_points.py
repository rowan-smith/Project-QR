from flask import Blueprint, render_template, session, abort
from flask_login import fresh_login_required

from models.User import User

points_blueprint = Blueprint('points_page', __name__)


@points_blueprint.route('/points', methods=['POST', 'GET'])
@fresh_login_required
def points():
    return render_template('user_points.html', users=User.query.order_by(User.points.desc()).all())
