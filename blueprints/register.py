import uuid

from flask import Blueprint, render_template, request, session, redirect
from flask_login import login_user

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

        # User register creation
        user = User()
        user.id = str(uuid.uuid4())
        user.name = request.form['name']
        user.username = request.form['username']
        user.email = request.form['email']
        user.password_hash = User.set_password(request.form['password'])

        # Add user to SQLAlchemy
        db.session.add(user)
        db.session.commit()

        # Add user info to session for use later in HTML
        session['username'] = user.username
        session['points'] = user.points
        session['name'] = user.name
        session['email'] = user.email

        # TODO check for remember me functionality.
        login_user(user, remember=True)

        return redirect('home')

    return render_template('register_page.html')
