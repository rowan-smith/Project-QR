from flask import Blueprint, render_template, session, abort

from models.ScanLocation import ScanLocation

locations_blueprint = Blueprint('locations_page', __name__)

QR_URL = "http://127.0.0.1/qr?url="
SCAN_URL = "http://127.0.0.1/scan?location="


@locations_blueprint.route('/locations')
def locations():

    if 'username' in session and session['is_admin']:
        return render_template('locations.html', locations=ScanLocation.query.all(), scan_url=SCAN_URL, qr_url=QR_URL)

    abort(404)
