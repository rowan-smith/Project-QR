from flask import Blueprint, render_template, session, request

from models.User import User

login_blueprint = Blueprint('login_page', __name__)


@login_blueprint.route('/login', methods=['POST', 'GET'])
def login_page():

    if session.get('logged_in') is None:

        if request.method == 'POST':

            # Check if username is in database
            user = User.query.filter_by(username=request.form['user-username']).first()
            if user is None:
                error = "The username or password was invalid!"
                return render_template('login_page.html', error=error)

            # Check if password matches
            if not user.check_password(request.form['user-pass']):
                error = "The username or password was invalid!"
                return render_template('login_page.html', error=error)

            ############################################################
            # Initiate user login
            # TODO CREATE SECURE SESSION HERE
            # TODO CREATE PERMANENT SESSION COOKIE
            session['username'] = request.form['user-username']

            if user.is_admin:
                session['is_admin'] = True
            else:
                session['is_admin'] = False
            ############################################################

            return render_template('home.html', user=user)

        return render_template('login_page.html')

    return render_template('home.html')
