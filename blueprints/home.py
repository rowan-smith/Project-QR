from flask import Blueprint, render_template
from flask_login import fresh_login_required

home_blueprint = Blueprint('home_page', __name__)


@home_blueprint.route('/home')
@fresh_login_required
def home():
    return render_template('home.html')
