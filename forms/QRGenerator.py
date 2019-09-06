from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class QRGenerator(FlaskForm):
    code_content = StringField('Content', validators=[DataRequired()])
    code_size = SelectField('Size', choices=[('5', '5'),
                                             ('10', '10'),
                                             ('15', '15'),
                                             ('20', '20')])
    code_color = SelectField('Colour', choices=[("white", "White"),
                                                ('yellow', "Yellow"),
                                                ("#ffa500", "Orange")])
    code_image = StringField('Image URL')
    generate_code = SubmitField('Generate QR Code')
