import uuid

from flask import Blueprint, render_template, request, session

from models.User import User
from app import db
from flask import Markup

register_blueprint = Blueprint('register_page', __name__)


@register_blueprint.route('/register', methods=['POST', 'GET'])
def register_page():
    if request.method == 'POST':

        if User.query.filter_by(username=request.form['user-username']).first() is not None:
            error = f"The username <b>{request.form['user-username']}</b> already exists. Please choose another!"
            return render_template('register_page.html', error=Markup(error))

        if User.query.filter_by(email=request.form['user-email']).first() is not None:
            error = f"The email <b>{request.form['user-email']}</b> already exists. Please choose another!"
            return render_template('register_page.html', error=Markup(error))

        db.session.add(User(uuid=str(uuid.uuid4()),
                            name=request.form['user-name'],
                            username=request.form['user-username'],
                            email=request.form['user-email'],
                            password_hash=User.set_password(request.form['user-pass'])))
        db.session.commit()

        session['username'] = request.form['user-username']
        session['is_admin'] = False

        return render_template('home.html', session=session)

    return render_template('register_page.html')
