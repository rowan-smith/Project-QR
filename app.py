import os

from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_qrcode import QRcode

from instance.DevelopmentConfig import DevelopmentConfig
from instance.ProductionConfig import ProductionConfig

DATABASE_NAME = "QR-Users.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = os.urandom(24)
app.secret_key = 'JIRN#@UNT#@(UTH@#(GN@#*'

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


# Error handle 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(f"Page not found: {request.path}")
    return render_template("errors/404.html"), 404

# Error handle 500 (Internal Server Error)
@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error(f"Server Error: {error}")
    return render_template("errors/500.html"), 500

# Error handle 401 (Unauthorized Access)
@app.errorhandler(401)
def unauthorized_access(error):
    app.logger.error(f"Server Error: {error}")
    return render_template("errors/401.html"), 401

# Error handle all
@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error(f"Unhandled Exception: {error}")
    return render_template('errors/UnknownError.html')

# Login Manager (Gets User Information)
@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)


if __name__ == '__main__':
    app.run(debug=True, port=80)
