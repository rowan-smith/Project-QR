import uuid

from app import db
from models.ScanLocation import ScanLocation

db.session.add_all([
    ScanLocation(name='Education Central', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Eddie Koiki Mabo Library', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Sir Geroge Kneipp Auditorium', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Faculty of Science and Engineering', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Student Association', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='The Science Place', bonus=False, uuid=uuid.uuid4().hex, points=1),
    ScanLocation(name='Nursing Sciences', bonus=False, uuid=uuid.uuid4().hex, points=1)
])

db.session.commit()
