import uuid

from flask import Blueprint, render_template, request

from User import User
from app import db

register_blueprint = Blueprint('register_page', __name__)


@register_blueprint.route('/register', methods=['POST', 'GET'])
def register_page():

    if request.method == 'POST':

        if User.query.filter_by(username=request.form['user-username']).first() is not None:
            error = f"The username {request.form['user-username']} already exists. Please choose another!"
            return render_template('register_page.html', error=error)

        if User.query.filter_by(email=request.form['user-email']).first() is not None:
            error = f"The email {request.form['user-email']} already exists. Please choose another!"
            return render_template('register_page.html', error=error)

        db.session.add(User(id=str(uuid.uuid4()),
                            name=request.form['user-name'],
                            username=request.form['user-username'],
                            email=request.form['user-email'],
                            password_hash=User.set_password(request.form['user-pass'])))

        db.session.commit()

    return render_template('register_page.html')
