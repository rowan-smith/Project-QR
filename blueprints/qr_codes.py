from flask import Blueprint, render_template, session, abort, url_for

from models.QrCodes import QrCodes

locations_blueprint = Blueprint('qr_codes', __name__)

QR_URL = "http://127.0.0.1/qr?url="
SCAN_URL = "http://127.0.0.1/scan?qr_code="


@locations_blueprint.route('/qr_codes')
def qr_codes():

    # return url_for('home_page.home', my_var='my_value', test='test')

    # return url_for('qr_generator_page.qr_code', url=url_for('qr_code_page.qr_scan', qr_code=i.uuid))

    if 'username' in session and session['is_admin']:
        return render_template('qr_codes.html', qr_codes=QrCodes.query.all(), scan_url=SCAN_URL, qr_url=QR_URL)

    abort(404)
