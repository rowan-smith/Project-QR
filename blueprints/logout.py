from flask import Blueprint, session, redirect
from flask_login import login_required, logout_user

logout_blueprint = Blueprint('logout_page', __name__)


@logout_blueprint.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    # Logs current user out
    logout_user()

    # Clears all session information
    session.clear()

    return redirect('/')
