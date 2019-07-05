from flask import Blueprint, render_template, session, abort

from models.User import User

points_blueprint = Blueprint('points_page', __name__)


@points_blueprint.route('/points', methods=['POST', 'GET'])
def points():

    if 'username' in session and session['is_admin']:

        return render_template('user_points.html', users=User.query.order_by(User.points.desc()).all())

    abort(404)
