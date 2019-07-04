from flask import Blueprint, render_template, request

qr_code_blueprint = Blueprint('qr_code_page', __name__)


@qr_code_blueprint.route('/code', methods=['GET'])
def qr_scanner():
    data = request.values

    # TODO ADD LIST OF BUILDINGS AND CHECK QR CODES AGAIN BUILDING

    print(data['building'])
    # for datum in data:
    #     print(datum[''])
    #
    return render_template('qr_scanner.html')
