import uuid

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    # User admin information
    uuid = db.Column(db.String(36), unique=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)

    # User game information
    points = db.Column(db.Integer, nullable=True)
    scanned_qr_codes = db.Column(db.String(300), nullable=True)

    def __init__(self, name: str, username: str, email: str, password: str, is_admin: bool = False):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.username = username
        self.email = email
        self.password_hash = self.set_password(password)
        self.is_admin = is_admin

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.uuid

    def __repr__(self):
        return f'<User {self.username}>'
