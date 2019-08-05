from flask import Blueprint, render_template, request, session, abort, redirect

from models.User import User
from models.QrCodes import QrCodes
from app import db

qr_code_blueprint = Blueprint('qr_code_scan_page', __name__)


@qr_code_blueprint.route('/scan', methods=['GET'])
def qr_scan():
    if 'username' in session:

        if len(request.values) == 0:
            return render_template('qr_scanner.html')

        qr_code = QrCodes.query.filter_by(uuid=request.values['qr_code']).first()

        ##########################################################
        user = User.query.filter_by(username=session['username']).first()

        if user.scanned_qr_codes is None:
            qr_code_list = []
            user.scanned_qr_codes = f"{qr_code.id},"
        else:
            qr_code_list = user.scanned_qr_codes.split(",")
            user.scanned_qr_codes += f"{qr_code.id},"

        if str(qr_code.id) in qr_code_list:
            return render_template('qr_scanner.html')

        if not user.points:
            user.points = qr_code.points
        else:
            user.points += qr_code.points

        db.session.commit()
        ##########################################################

        if not qr_code:
            return render_template('qr_scanner.html')

        return render_template('qr_scanner.html', qr_code=qr_code)
    return redirect('login')
