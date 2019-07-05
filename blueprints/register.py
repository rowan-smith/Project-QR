import uuid

from flask import Blueprint, render_template, request

from models.User import User
from app import db

register_blueprint = Blueprint('register_page', __name__)


@register_blueprint.route('/register', methods=['POST', 'GET'])
def register_page():
    if request.method == 'POST':

        if User.query.filter_by(username=request.form['user-username']).first() is not None:
            return render_template('register_page.html',
                                   error_msg_start="The username",
                                   duplicate_value=request.form['user-username'],
                                   error_msg_end="already exists. Please choose another!")

        if User.query.filter_by(email=request.form['user-email']).first() is not None:
            return render_template('register_page.html',
                                   error_msg_start="The email",
                                   duplicate_value=request.form['user-email'],
                                   error_msg_end="already exists. Please choose another!")

        user = User(uuid=str(uuid.uuid4()),
                    name=request.form['user-name'],
                    username=request.form['user-username'],
                    email=request.form['user-email'],
                    password_hash=User.set_password(request.form['user-pass']))

        db.session.add(user)

        db.session.commit()

        return render_template('home.html', user=user)

    return render_template('register_page.html')
