from flask import Blueprint, render_template, session, flash

login_blueprint = Blueprint('login_page', __name__)


@login_blueprint.route('/login')
def login_page():
    x = None
    if x:
        session['logged_in'] = True
        return render_template('home.html')
    else:
        flash('wrong password!')
        return render_template('login_page.html')
