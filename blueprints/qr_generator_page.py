from flask import Blueprint, render_template

qr_gen_blueprint = Blueprint('qr_generator_page', __name__)


@qr_gen_blueprint.route('/qr')
@qr_gen_blueprint.route('/qr/<url>')
@qr_gen_blueprint.route('/qr/<url>/<colour>')
@qr_gen_blueprint.route('/qr/<url>/<colour>/<size>')
def qr_page(url: str = "it.jcu.io", colour: str = "white", size: int = 60):
    return render_template('qr_generator.html', url=url, colour=colour, size=size)
