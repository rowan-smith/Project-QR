from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class QRCreator(FlaskForm):
    code_name = StringField('QR Code Name', validators=[DataRequired()])
    code_points = IntegerField('QR Code Points', validators=[DataRequired()])
    create_code = SubmitField('Create QR Code')
