from flask import render_template, Blueprint, request, session, abort, redirect, url_for, escape
from flask_login import login_required

from app import db
from forms import QRCreator
from models import QRModel, UserModel

qr = Blueprint('qr', __name__)

QR_URL = "http://127.0.0.1"
SCAN_URL = "https://timtamtime.pythonanywhere.com"


@qr.route('/qr/codes/', methods=['POST', 'GET'])
@login_required
def _codes():

    if session["is_admin"]:
        form = QRCreator()
        if form.validate_on_submit():

            # Check if QR already exists.
            if QRModel.query.filter_by(name=form.code_name.data).first():
                return render_template("QR/codes.html", qr_codes=QRModel.query.all(), form=form)

            db.session.add(QRModel(form.code_name.data, form.code_points.data))
            db.session.commit()
            return redirect(url_for('qr._codes'))

        return render_template('QR/codes.html', qr_codes=QRModel.query.all(), form=form)
    abort(404)


@qr.route('/qr/generator/')
@qr.route('/qr/generator/<string:content>/')
@qr.route('/qr/generator/<string:content>/<int:size>/')
@login_required
def _generator(*, content: str = SCAN_URL, size: int = 15, colour: str = 'white', image: str = 'images/IT@JCU Logo.jpg'):

    if session["is_admin"]:
        return render_template('QR/generator.html', url=f"{SCAN_URL}{url_for('qr._scanner')}?code={content}",
                               size=size, colour=colour, image=image)
    abort(404)


@qr.route('/qr/scanner/')
@login_required
def _scanner():
    if len(request.values) == 0:
        return render_template('QR/scanner.html')

    qr_code = QRModel.query.filter_by(uuid=request.values['code']).first()

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

    session['points'] = user.points
    ##########################################################

    return render_template('QR/scanner.html', code=qr_code)
