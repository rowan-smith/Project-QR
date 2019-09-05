from datetime import timedelta

from flask import render_template, redirect, url_for, Blueprint, request, abort, session
from flask_login import current_user, login_user, logout_user

from app import db
from models.UserModel import UserModel
from forms import LoginForm
from forms import RegistrationForm

auth = Blueprint('auth', __name__)


@auth.route('/signin', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
def _login():
    if current_user.is_authenticated:
        return redirect(url_for('account._account'))

    form = LoginForm()
    if form.validate_on_submit():

        # Checks if user exists
        user = UserModel.query.filter_by(username=request.form['username']).first()

        # Checks if password matches.
        if not user.check_password(request.form['password']):
            abort(401)

        try:
            if request.form['remember_me'] == 'y':
                login_user(user, remember=True, fresh=True, duration=timedelta(days=90))
            else:
                login_user(user, remember=False, fresh=True, duration=timedelta(days=90))
        except KeyError:
            login_user(user, remember=False, fresh=True, duration=timedelta(days=90))

        session['name'] = user.name
        session['username'] = user.username
        session['email'] = user.email
        session['points'] = user.points
        session.permanent = True

        if user.is_admin:
            session['is_admin'] = True
        else:
            session['is_admin'] = False

        return redirect(url_for('account._account'))

    return render_template('auth/login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
@auth.route('/register', methods=['GET', 'POST'])
def _register():
    if current_user.is_authenticated:
        return redirect(url_for('account._account'))

    form = RegistrationForm()
    if form.validate_on_submit():

        ####################################################

        # # Check if username already exists in database
        # if UserModel.query.filter_by(username=form.username.raw_data).first() is not None:
        #     return render_template('auth/register.html')
        #
        # # # Check if email already exists in database
        # if UserModel.query.filter_by(email=form.email.raw_data).first() is not None:
        #     return render_template('auth/register.html')

        # User register creation and user add to SQLAlchemy
        db.session.add(UserModel(form.name.raw_data,
                                 form.username.raw_data,
                                 form.email.raw_data,
                                 form.password.raw_data))
        db.session.commit()

        # Add user info to session for use later in HTML
        session['name'] = form.name.raw_data
        session['username'] = form.username.raw_data
        session['email'] = form.username.raw_data
        session['points'] = None

        try:
            if request.form['remember_me'] == 'y':
                login_user(UserModel.query.filter_by(name=session['name']).first(), True)
            else:
                login_user(UserModel.query.filter_by(name=session['name']).first(), False)
        except KeyError:
            login_user(UserModel.query.filter_by(name=session['name']).first(), False)

        # Log user in
        return redirect(url_for('account._account'))

    return render_template('auth/register.html', form=form)


@auth.route('/signout')
@auth.route('/logout')
def _logout():
    # Logs current user out
    logout_user()

    # Clears all session information
    session.clear()

    # Redirect to Index Page
    return redirect(url_for("index._index"))
