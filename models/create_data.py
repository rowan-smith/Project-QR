import uuid

from app import db
from models.ScanLocation import ScanLocation
from models.User import User

db.session.add_all([
    ScanLocation(name='Education Central', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Eddie Koiki Mabo Library', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Sir Geroge Kneipp Auditorium', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Faculty of Science and Engineering', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Student Association', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='The Science Place', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Nursing Sciences', bonus=False, uuid=uuid.uuid4().hex, points=1)
])

db.session.add(User(uuid=str(uuid.uuid4()),
                    name='admin',
                    username='admin',
                    email='admin@admin',
                    password_hash=User.set_password('admin'),
                    is_admin=True))

db.session.commit()
