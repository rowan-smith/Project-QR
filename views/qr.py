from flask import render_template, Blueprint, request, session, abort, redirect, url_for, escape, flash
from flask_login import login_required

from app import db, app
from forms import QRCreator, QRGenerator, QRScanner
from models import QRModel, UserModel

qr = Blueprint('qr', __name__)


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


@qr.route('/qr/generator/', methods=['POST', 'GET'])
@qr.route('/qr/generator/<string:code_id>/', methods=['POST', 'GET'])
@login_required
def _generator(code_id: str = None):
    form = QRGenerator()
    if code_id is None:

        if form.validate_on_submit():
            data = {'CONTENT': form.code_content.data,
                    'SIZE': int(form.code_size.data),
                    'COLOR': form.code_color.data,
                    'CORRECTION': form.code_correction.data,
                    'IMAGE': form.code_image.data}

            return render_template("QR/generator.html", form=form, data=data)

        return render_template("QR/generator.html", form=form)

    else:
        if session['is_admin']:
            if app.config['DEBUG']:
                scan_url = f"http://127.0.0.1"
            else:
                scan_url = "https://timtamtime.pythonanywhere.com"

            data = {'CONTENT': f"{scan_url}{url_for('qr._scanner')}{code_id}/",
                    'SIZE': 20,
                    'COLOR': 'white',
                    'CORRECTION': 'H',
                    'IMAGE': 'images/IT@JCU Logo.jpg'}

            return render_template("QR/generator.html", data=data)
        else:
            return render_template("QR/generator.html", form=form)


@qr.route('/qr/scan/', methods=['POST', 'GET'])
@qr.route('/qr/scan/<string:code_id>/', methods=['POST', 'GET'])
@login_required
def _scanner(code_id: str = None):
    form = QRScanner()

    if code_id is None:
        return render_template('QR/scanner.html', form=form)

    qr_code = QRModel.query.filter_by(uuid=code_id).first()
    if qr_code is None:
        return render_template('QR/scanner.html', form=form)

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
            return render_template('QR/scanner.html', found=True)

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
