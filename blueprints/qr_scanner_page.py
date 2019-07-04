from flask import Blueprint, render_template, request

qr_code_blueprint = Blueprint('qr_code_page', __name__)

BUILDINGS = ['Education Central',
             'Eddie Koiki Mabo Library',
             'Sir George Kneipp Auditorium',
             'Faculty of Science and Engineering',
             'Student Association',
             'The Science Place',
             'Nursing Sciences']


@qr_code_blueprint.route('/code', methods=['GET'])
def qr_scanner():

    if request.values['building'] in BUILDINGS:
        # TODO SQL DATABASE COUNT HERE
        return render_template('qr_scanner.html', building=request.values['building'])

    else:
        return render_template('qr_scanner.html', building=None)
