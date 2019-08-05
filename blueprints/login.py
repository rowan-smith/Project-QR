from flask import Blueprint, render_template, session, request, Response, redirect, abort, flash
from flask_login import login_user
from app import app, login_manager
from models.LoginForm import LoginForm

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

        # check if user exists
        if user is None:
            abort(401)

        # Check if password is incorrect
        # TODO change from abort later
        if not user.check_password(request.form['password']):
            abort(401)

        # Logs in user
        login_user(user, remember=True)

        # sets user session information for use in HTML later
        session['name'] = user.name
        session['username'] = user.username
        session['email'] = user.email
        session['points'] = user.points

        return redirect('home')

    return render_template('login_page.html', form=LoginForm())


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
