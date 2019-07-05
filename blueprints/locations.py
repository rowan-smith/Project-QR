from flask import Blueprint, render_template

from models.ScanLocation import ScanLocation

locations_blueprint = Blueprint('locations_page', __name__)

# User.query.order_by(User.username.desc()).all()

QR_URL = "http://127.0.0.1/qr?url="
SCAN_URL = "http://127.0.0.1/scan?location="


@locations_blueprint.route('/locations')
def locations_page():
    return render_template('locations.html', locations=ScanLocation.query.all(), scan_url=SCAN_URL, qr_url=QR_URL)
