from flask import Blueprint, render_template, session

logout_blueprint = Blueprint('logout_page', __name__)


@logout_blueprint.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('username', None)
    session.pop('is_admin', None)
    return render_template('index.html')
