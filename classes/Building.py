from app import db


class Building(db.Model):

    __tablename__ = 'buildings'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
