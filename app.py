from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_page():
    return 'This is the page people first see.'


@app.route('/home')
def home_page():
    return 'This is the home page for users that are logged in.'


@app.route('/login')
def login_page():
    return 'This is the login page.'


if __name__ == '__main__':
    app.run()
