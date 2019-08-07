import uuid

from app import db
from models.QrCodes import QrCodes
from models.User import User

codes = []
for i in range(13):
    codes.append(QrCodes(f'Week {i+1}', 5))

codes.append(QrCodes('Pizza Bonus', 1))
codes.append(QrCodes('1 Bonus Point', 1))
codes.append(QrCodes('2 Bonus Points', 2))
codes.append(QrCodes('3 Bonus Points', 3))
codes.append(QrCodes('5 Bonus Points', 5))

db.session.add_all(codes)

if not User.query.filter_by(name='admin').first():
    db.session.add_all([User('admin', 'admin', 'admin@admin', 'admin', True)])

db.session.commit()
