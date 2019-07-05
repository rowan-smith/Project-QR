import uuid

from app import db


class ScanLocation(db.Model):

    __tablename__ = 'locations'

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    bonus = db.Column(db.Boolean, nullable=True)
    uuid = db.Column(db.String(32))

    def get_location_hash(self):
        return self.unique_hash

    def get_name(self):
        return self.name

    def is_bonus(self):
        return self.bonus

    def __repr__(self):
        return f'<ScanLocation {self.name}>'


if __name__ == '__main__':

    scan = ScanLocation(name='The Science Place', bonus=False, uuid=uuid.uuid4().hex)

    print(scan.name)

    db.session.add(ScanLocation(name='The Science Place', bonus=False, uuid=uuid.uuid4().hex))

    db.create_all()
