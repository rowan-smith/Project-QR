from flask import Blueprint, render_template, request

from models.ScanLocation import ScanLocation

qr_code_blueprint = Blueprint('qr_code_page', __name__)


@qr_code_blueprint.route('/scan', methods=['GET'])
def qr_scanner():

    if len(request.values) == 0:
        return render_template('qr_scanner.html')

    location = ScanLocation.query.filter_by(uuid=request.values['location']).first()

    if not location:
        return render_template('qr_scanner.html')

    return render_template('qr_scanner.html', location=location)
