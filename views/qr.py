from flask import render_template, Blueprint, request, session
from flask_login import login_required

from app import db
from models import QRModel, UserModel

qr = Blueprint('qr', __name__)


@qr.route('/qr/codes')
@login_required
def _codes():
    QR_URL = "http://127.0.0.1/qr?url="
    SCAN_URL = "https://timtamtime.pythonanywhere.com/scan?qr_code="
    return render_template('QR/codes.html', qr_codes=QRModel.query.all(), scan_url=SCAN_URL, qr_url=QR_URL)


@qr.route('/qr/generator')
@login_required
def _generator():
    data = {
        'url': 'it.jcu.io',
        'size': 15,
        'colour': 'white',
        'image': 'default'
    }

    temp_data = dict(request.values)
    for i in temp_data:

        if str(i).lower() == 'image':
            data['image'] = temp_data[i]

        if str(i).lower() == 'size':
            data['size'] = temp_data[i]

        if str(i).lower() == 'colour' or str(i).lower() == 'color':
            data['colour'] = temp_data[i]

        if str(i).lower() == 'url':
            data['url'] = temp_data[i]
    del temp_data

    return render_template('QR/generator.html', data=data)


@qr.route('/qr/scanner')
@login_required
def _scanner():
    if len(request.values) == 0:
        return render_template('QR/scanner.html')

    qr_code = QRModel.query.filter_by(uuid=request.values['qr_code']).first()

    ##########################################################
    user = UserModel.query.filter_by(username=session['username']).first()

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
            return render_template('QR/scanner.html')

    # If QR code is able to be scanned multiple times
    else:
        if not user.points:
            user.points = qr_code.points
        else:
            user.points += qr_code.points

    db.session.commit()
    ##########################################################

    return render_template('QR/scanner.html', qr_code=qr_code)


@qr.route("/qr/creator")
@login_required
def _creator():
    return render_template("QR/creator.html")
