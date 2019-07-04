from flask import Blueprint, render_template

index_blueprint = Blueprint('index_page', __name__)


@index_blueprint.route('/')
def index_page():
    return render_template('index.html')
