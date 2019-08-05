from flask import Blueprint, render_template, request, session, abort, redirect
from flask_login import fresh_login_required

from models.User import User
from models.QrCodes import QrCodes
from app import db

qr_code_blueprint = Blueprint('qr_code_scan_page', __name__)


@qr_code_blueprint.route('/scan', methods=['GET'])
@fresh_login_required
def qr_scan():

    if len(request.values) == 0:
        return render_template('qr_scanner.html')

    qr_code = QrCodes.query.filter_by(uuid=request.values['qr_code']).first()

    ##########################################################
    user = User.query.filter_by(username=session['username']).first()

    # If qr code can only be scanned once (first 13 values (weeks) in the Qr code table can only be scanned once)
    if qr_code.id < 14:
        if user.scanned_qr_codes is None:
            qr_code_list = []
            user.scanned_qr_codes = f"{qr_code.id},"
        else:
            qr_code_list = user.scanned_qr_codes.split(",")
            user.scanned_qr_codes += f"{qr_code.id},"

        if not user.points:
            user.points = qr_code.points
        else:
            user.points += qr_code.points

        if str(qr_code.id) in qr_code_list:
            return render_template('qr_scanner.html')

    # If QR code is able to be scanned multiple times
    else:
        if not user.points:
            user.points = qr_code.points
        else:
            user.points += qr_code.points

    db.session.commit()
    ##########################################################

    return render_template('qr_scanner.html', qr_code=qr_code)
