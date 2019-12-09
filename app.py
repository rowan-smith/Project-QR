from flask import Flask, render_template, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_qrcode import QRcode

from config import ProductionConfig, DevelopmentConfig

app = Flask(__name__)

db = SQLAlchemy(app)
QRcode(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.session_protection = "strong"
# login_manager.login_view = "auth._login"

# Load Database
if app.config['DEBUG']:
    app.config.from_object(DevelopmentConfig())
else:
    app.config.from_object(ProductionConfig())

# Import all blueprints
from views import *

# Create Database
from models import UserModel
db.create_all()

if db.session.query(UserModel).first() is None:
    db.session.add_all([UserModel('admin', 'admin', 'admin@admin', 'admin', True)])
    db.session.commit()

# New Blueprints
app.register_blueprint(index)
app.register_blueprint(auth)
app.register_blueprint(account)
app.register_blueprint(qr)
app.register_blueprint(leaderboard)
app.register_blueprint(admin)

# Error handle 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

# Error handle 500 (Internal Server Error)
@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error(f"Internal Server Error: {error}")
    return render_template("errors/500.html"), 500

# Error handle 401 (Unauthorized Access)
@app.errorhandler(401)
def unauthorized_access(error):
    app.logger.error(f"Unauthorized Access: {error}")
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


# @app.before_request
# def load_logged_in_user():
#     user = UserModel.query.filter_by(name=session.get("name")).first()


if __name__ == '__main__':
    app.run()
