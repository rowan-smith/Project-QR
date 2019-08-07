import uuid

from app import db
from models.QrCodes import QrCodes
from models.User import User

db.session.add_all([
    # Weeks 2-13 Codes
    QrCodes('Week 1', 5),
    QrCodes('Week 2', 5),
    QrCodes('Week 3', 5),
    QrCodes('Week 4', 5),
    QrCodes('Week 5', 5),
    QrCodes('Week 6', 5),
    QrCodes('Week 7', 5),
    QrCodes('Week 8', 5),
    QrCodes('Week 9', 5),
    QrCodes('Week 10', 5),
    QrCodes('Week 11', 5),
    QrCodes('Week 12', 5),
    QrCodes('Week 13', 5),

    # Bonus Points
    QrCodes('Pizza Bonus', 1),
    QrCodes('1 Bonus Point', 1),
    QrCodes('2 Bonus Points', 2),
    QrCodes('3 Bonus Points', 3),
    QrCodes('5 Bonus Points', 5),
])

if not User.query.filter_by(name='admin').first():
    u = User()
    u.name = 'admin'
    u.username = 'admin'
    u.email = 'admin@admin'
    u.id = str(uuid.uuid4())
    u.password_hash = u.set_password('admin')
    u.is_admin = True

    db.session.add_all([u])

db.session.commit()
