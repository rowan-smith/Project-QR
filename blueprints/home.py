from flask import Blueprint, render_template, session, url_for, redirect

home_blueprint = Blueprint('home_page', __name__)


@home_blueprint.route('/home')
def home_page():

    if 'username' in session:
        return render_template('home.html', session=session)
    return 'You are not logged in'

    # if session.get('logged_in') is None:
    #     return redirect(url_for('login_page.login_page'))
    #
    # return render_template('home.html')
