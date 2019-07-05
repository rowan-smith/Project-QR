from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):

    __tablename__ = 'users'

    # User admin information
    uuid = db.Column(db.String(36), unique=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    # User game information
    points = db.Column(db.Integer, nullable=True)

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
