from flask import Blueprint, render_template
from flask_login import fresh_login_required
from flask import Blueprint, render_template, session, url_for, redirect
from models.User import User

home_blueprint = Blueprint('home_page', __name__)


@home_blueprint.route('/home')
@fresh_login_required
def home():
    return render_template('home.html')
    if 'username' in session:
        session['points'] = User.query.filter_by(name=session['name']).first().points
        return render_template('home.html', session=session, users=User.query.order_by(User.points.desc()).all())

    return redirect(url_for('login_page.login'))
