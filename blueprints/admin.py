from flask import Blueprint, render_template, session, abort

admin_blueprint = Blueprint('admin_page', __name__)


@admin_blueprint.route('/admin', methods=['POST', 'GET'])
def admin():

    if 'username' in session and session['is_admin']:
        return render_template('admin.html')

    abort(404)
