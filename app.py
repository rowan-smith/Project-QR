from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/home')
def home_page():

    # Check is flask session is active
    if session is None:
        return redirect(url_for('login_page'))

    return render_template('home.html')


@app.route('/login')
def login_page():
    return render_template('login_page.html')


if __name__ == '__main__':
    app.run()
