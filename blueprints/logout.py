from flask import Blueprint, render_template, session

logout_blueprint = Blueprint('logout_page', __name__)


@logout_blueprint.route('/logout', methods=['POST', 'GET'])
def logout():

    # [session.pop(key) for key in list(session.keys())]

    session.clear()

    return render_template('index.html')