from flask import render_template, Blueprint
from flask_login import login_required

admin = Blueprint('admin', __name__)


@admin.route('/admin/')
@login_required
def _dashboard():
    return render_template("admin/dashboard.html")


@admin.route('/admin/users/')
@login_required
def _users():
    return render_template("admin/users.html")
