from flask import Blueprint, render_template, request, session, abort, redirect

from models.User import User
from models.ScanLocation import ScanLocation
from app import db

qr_code_blueprint = Blueprint('qr_code_page', __name__)


@qr_code_blueprint.route('/scan', methods=['GET'])
def qr_scan():
    if 'username' in session:

        if len(request.values) == 0:
            return render_template('qr_scanner.html')

        location = ScanLocation.query.filter_by(uuid=request.values['location']).first()

        ##########################################################
        user = User.query.filter_by(username=session['username']).first()

        if user.visited_locations is None:
            location_list = []
            user.visited_locations = f"{location.id},"
        else:
            location_list = user.visited_locations.split(",")
            user.visited_locations += f"{location.id},"

        if str(location.id) in location_list:
            return render_template('qr_scanner.html')

        if not user.points:
            user.points = location.points
        else:
            user.points += location.points

        db.session.commit()
        ##########################################################

        if not location:
            return render_template('qr_scanner.html')

        return render_template('qr_scanner.html', location=location)
    return redirect('login')
