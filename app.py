import os

from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_qrcode import QRcode

from config import ProductionConfig, DevelopmentConfig

app = Flask(__name__)
# app.secret_key = os.urandom(24)

db = SQLAlchemy(app)
QRcode(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.session_protection = "strong"
# login_manager.login_view = "login_page.login"

# Load Database
if os.environ['FLASK_ENV'] == 'production':
    app.config.from_object(ProductionConfig())
else:
    app.config.from_object(DevelopmentConfig())

# Import all blueprints
from views import *

# Create Database
from models import UserModel
db.create_all()
if not UserModel.query.filter_by(name='admin').first():
    db.session.add_all([UserModel('admin', 'admin', 'admin@admin', 'admin', True)])
db.session.commit()

# New Blueprints
app.register_blueprint(index)
app.register_blueprint(auth)
app.register_blueprint(account)
app.register_blueprint(qr)
app.register_blueprint(errors)


# Login Manager (Gets User Information)
@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)

#
# @app.before_request
# def load_logged_in_user():
#     user_id = session.get('user_id')
#
#     if user_id is None:
#         g.user = None
#     else:
#         g.user = get_db().execute(
#             'SELECT * FROM user WHERE id = ?', (user_id,)
#         ).fetchone()


if __name__ == '__main__':
    app.run(debug=True, port=80)
