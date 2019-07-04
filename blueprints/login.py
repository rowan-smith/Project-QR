from flask import Blueprint, render_template, session, request

# from User import User

login_blueprint = Blueprint('login_page', __name__)


@login_blueprint.route('/login', methods=['POST', 'GET'])
def login_page():

    # If session is none we want to create a session
    if session.get('logged_in') is None:

        if request.method == 'POST':

            # Check if username is in database
            # user = User.query.filter_by(username=request.form['user-username']).first()
            # is_user = user.check_password(request.form['user-pass'])
            #
            # if is_user:
            #     print("FUCK YES CUNT")



            # if request.form['user-username'] == 'Rono':
            #     print("Accepted")
            # else:
            #     return render_template('login_page.html', error="username or password is incorrect!")
            #
            # # Check if hash password matches hash in database
            # if request.form['user-pass'] == 'password':
            #     print("Accepted")
            # else:
            #     return render_template('login_page.html', error="username or password is incorrect!")
            #
            # # If hash matches create a permanent session and set session to true
            #
            # session['logged_in'] = True
            return render_template('home.html')

        if request.method == 'GET':
            return render_template('login_page.html')

    # If session is not none we want to load home
    else:
        return render_template('home.html')
