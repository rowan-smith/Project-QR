from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class QRScanner(FlaskForm):
    code = StringField('Code', validators=[DataRequired()])
    generate_code = SubmitField('Scan Code')
