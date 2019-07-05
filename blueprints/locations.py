from flask import Blueprint, render_template

from models.ScanLocation import ScanLocation

locations_blueprint = Blueprint('locations_page', __name__)

# User.query.order_by(User.username.desc()).all()


@locations_blueprint.route('/locations')
def locations_page():
    return render_template('locations.html', locations=ScanLocation.query.all())
