from datetime import timedelta

from flask import render_template, redirect, url_for, Blueprint, request, abort, session, flash
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

        # Check if username already exists in database
        if user is None:
            flash('username does not exist')
            return render_template('auth/login.html', form=form)

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

        # Check if username already exists in database
        if UserModel.query.filter_by(username=form.username.raw_data[0]).first() is not None:
            flash('Username already exists')
            return render_template('auth/register.html', form=form)

        # Check if email already exists in database
        if UserModel.query.filter_by(email=form.email.raw_data[0]).first() is not None:
            flash('Email already exists')
            return render_template('auth/register.html', form=form)

        # User register creation and user add to SQLAlchemy
        db.session.add(UserModel(form.name.raw_data[0],
                                 form.username.raw_data[0],
                                 form.email.raw_data[0],
                                 form.password.raw_data[0]))
        db.session.commit()

        # Add user info to session for use later in HTML
        session['name'] = form.name.raw_data[0]
        session['username'] = form.username.raw_data[0]
        session['email'] = form.username.raw_data[0]
        session['points'] = None
        session.permanent = True

        try:
            if request.form['remember_me'] == 'y':
                login_user(UserModel.query.filter_by(name=session['name']).first(), remember=True, fresh=True, duration=timedelta(days=90))
            else:
                login_user(UserModel.query.filter_by(name=session['name']).first(), remember=False, fresh=True, duration=timedelta(days=90))
        except KeyError:
            login_user(UserModel.query.filter_by(name=session['name']).first(), remember=False, fresh=True, duration=timedelta(days=90))

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
