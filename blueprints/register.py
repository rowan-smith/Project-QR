from flask import Blueprint, render_template, request, session, redirect
from flask_login import login_user

from forms.RegistrationForm import RegistrationForm
from models.User import User
from app import db

register_blueprint = Blueprint('register_page', __name__)


@register_blueprint.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':

        # TODO fix whatever is happening in the two block below.
        #  Flash message when the two blocks happen, combine into one?

        # Check if username already exists in database
        if User.query.filter_by(username=request.form['username']).first() is not None:
            return render_template('register_page.html')

        # Check if email already exists in database
        if User.query.filter_by(email=request.form['email']).first() is not None:
            return render_template('register_page.html')

        # User register creation and user add to SQLAlchemy
        db.session.add(User(request.form['name'],
                            request.form['username'],
                            request.form['email'],
                            request.form['password']))
        db.session.commit()

        # Add user info to session for use later in HTML
        session['name'] = request.form['name']
        session['username'] = request.form['username']
        session['email'] = request.form['email']
        session['points'] = None

        # TODO check for remember me functionality.
        login_user(User.query.filter_by(name=session['name']).first(), remember=True)

        return redirect('home')

    return render_template('register_page.html', form=RegistrationForm())
