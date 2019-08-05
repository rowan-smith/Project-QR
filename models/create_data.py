import uuid

from app import db
from models.QrCodes import QrCodes
from models.User import User

db.session.add_all([
    # Weeks 2-13 Codes
    QrCodes(name='Week 1', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 2', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 3', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 4', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 5', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 6', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 7', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 8', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 9', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 10', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 11', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 12', uuid=uuid.uuid4().hex, points=5),
    QrCodes(name='Week 13', uuid=uuid.uuid4().hex, points=5),

    # Bonus Points
    QrCodes(name='Pizza Bonus', uuid=uuid.uuid4().hex, points=1),
    QrCodes(name='1 Bonus Point', uuid=uuid.uuid4().hex, points=1),
    QrCodes(name='2 Bonus Points', uuid=uuid.uuid4().hex, points=2),
    QrCodes(name='3 Bonus Points', uuid=uuid.uuid4().hex, points=3),
    QrCodes(name='5 Bonus Points', uuid=uuid.uuid4().hex, points=5),
])

db.session.add(User(uuid=str(uuid.uuid4()),
                    name='admin',
                    username='admin',
                    email='admin@admin',
                    password_hash=User.set_password('admin'),
                    is_admin=True))

db.session.commit()
