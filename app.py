import os

from flask import Flask, render_template, redirect, url_for, session, request, flash

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/home')
def home_page():

    if session.get('logged_in') is None:
        return redirect(url_for('login_page'))

    return render_template('home.html')


@app.route('/login')
def login_page():
    x = None
    if x:
        session['logged_in'] = True
        return render_template('home.html')
    else:
        flash('wrong password!')
        return render_template('login_page.html')


@app.route('/register')
def register_page():
    return render_template('register_page.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run()
