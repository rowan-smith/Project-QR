from flask import Blueprint, render_template

qr_blueprint = Blueprint('qr_page', __name__)


@qr_blueprint.route('/qr')
def qr_page():
    return render_template('qrtest.html')
