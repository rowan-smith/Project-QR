import uuid

from app import db


class QrCodes(db.Model):

    __tablename__ = 'qr_codes'

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    uuid = db.Column(db.String(32))

    points = db.Column(db.Integer)

    def get_location_hash(self):
        return self.unique_hash

    def get_name(self):
        return self.name

    def is_bonus(self):
        return self.bonus

    def __repr__(self):
        return f'<QrCodes {self.name}>'
