import uuid

from app import db
from models.QRModel import QRModel
from models.UserModel import UserModel

codes = []
for i in range(13):
    codes.append(QRModel(f'Week {i + 1}', 5))

codes.append(QRModel('Pizza Bonus', 1))
codes.append(QRModel('1 Bonus Point', 1))
codes.append(QRModel('2 Bonus Points', 2))
codes.append(QRModel('3 Bonus Points', 3))
codes.append(QRModel('5 Bonus Points', 5))

db.session.add_all(codes)

if not UserModel.query.filter_by(name='admin').first():
    db.session.add_all([UserModel('admin', 'admin', 'admin@admin', 'admin', True)])

db.session.commit()
