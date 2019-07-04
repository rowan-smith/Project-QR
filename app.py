from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/home/<name>')
def home_page(name: str):
    return render_template('home.html', name=name)


@app.route('/login')
def login_page():
    return 'This is the login page.'


if __name__ == '__main__':
    app.run()
