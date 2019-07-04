from flask import Blueprint, render_template

qr_blueprint = Blueprint('qr_page', __name__)


@qr_blueprint.route('/qr')
@qr_blueprint.route('/qr/<url>')
@qr_blueprint.route('/qr/<url>/<colour>')
@qr_blueprint.route('/qr/<url>/<colour>/<size>')
def qr_page(url: str = "it.jcu.io", colour: str = "white", size: int = 60):
    return render_template('qrtest.html', url=url, colour=colour, size=size)
