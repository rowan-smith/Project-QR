from flask import Blueprint, render_template

register_blueprint = Blueprint('register_page', __name__)


@register_blueprint.route('/register')
def register_page():
    return render_template('register_page.html')
