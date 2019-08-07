import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_qrcode import QRcode

from flask_nav import Nav
from flask_nav.elements import *
from wtforms import Label

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
login_manager.login_view = "login_page.login"

nav = Nav()
nav.init_app(app)
Bootstrap(app)

from blueprints.home import home_blueprint
from blueprints.index import index_blueprint
from blueprints.login import login_blueprint
from blueprints.register import register_blueprint
from blueprints.qr_generator_page import qr_gen_blueprint
from blueprints.qr_scanner_page import qr_code_blueprint
from blueprints.qr_codes import locations_blueprint
from blueprints.logout import logout_blueprint

db.create_all()

app.register_blueprint(home_blueprint)
app.register_blueprint(index_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(qr_gen_blueprint)
app.register_blueprint(qr_code_blueprint)
app.register_blueprint(locations_blueprint)
app.register_blueprint(logout_blueprint)


@nav.navigation()
def anonymous_nav():
    return Navbar(None,
                  View('Home', 'index_page.index'),
                  View('Login', 'login_page.login'),
                  View('Register', 'register_page.register'))


@nav.navigation()
def admin_nav():
    return Navbar(None,
                  View('Home', 'index_page.index'),
                  View('Account', 'home_page.home'),
                  Subgroup('QR',
                           View('QR Codes', 'qr_codes_page.qr_codes'),
                           View('QR Generator', 'qr_generator_page.generate_qr_code'),
                           View('QR Scanner', 'qr_code_scan_page.qr_scan')),
                  Subgroup('Admin',
                           View('Admin List', 'home_page.home')),
                  View('Logout', 'logout_page.logout'))


@nav.navigation()
def user_nav():
    return Navbar(None,
                  View('Home', 'index_page.index'),
                  View('Account', 'home_page.home'),
                  View('Logout', 'logout_page.logout'))


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True, port=80)
