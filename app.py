import os

from flask import Flask

from blueprints.index import index_blueprint
from blueprints.home import home_blueprint
from blueprints.login import login_blueprint
from blueprints.register import register_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(index_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(register_blueprint)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
