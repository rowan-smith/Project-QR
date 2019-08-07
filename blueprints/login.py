from flask import Blueprint, render_template, session, request, redirect, abort
from flask_login import login_user
from app import app, login_manager
from forms.LoginForm import LoginForm
from flask import Blueprint, render_template, session, request, url_for, redirect

from models.User import User

login_blueprint = Blueprint('login_page', __name__)


@app.errorhandler(401)
def page_not_found(e):
    return redirect('login')


@login_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        # Checks if user exists in database
        user = User.query.filter_by(username=request.form['username']).first()

        # TODO flash message if the two blocks below throw an error
        #  instead of aborting

        # check if user exists
        if user is None:
            abort(401)

        # Check if password is incorrect
        # TODO change from abort later
        if not user.check_password(request.form['password']):
            abort(401)

        # Logs in user
        # TODO check for remember me functionality.
        login_user(user, remember=True)

        # sets user session information for use in HTML later
        session['name'] = user.name
        session['username'] = user.username
        session['email'] = user.email
        session['points'] = user.points

        # TODO Remove is_admin
        if user.is_admin:
            session['is_admin'] = True
        else:
            session['is_admin'] = False

        return redirect('home')

    return render_template('login_page.html', form=LoginForm())


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
