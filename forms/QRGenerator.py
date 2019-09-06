from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class QRGenerator(FlaskForm):
    code_content = StringField('Content', validators=[DataRequired()])
    code_size = SelectField('Size', choices=[('15', 'Size'),
                                             ('5', '5'),
                                             ('10', '10'),
                                             ('15', '15'),
                                             ('20', '20'),
                                             ('25', '25'),
                                             ('30', '30')])
    code_color = SelectField('Colour', choices=[('white', 'Colour'),
                                                ("white", "White"),
                                                ('yellow', "Yellow"),
                                                ('lime', "Green"),
                                                ("#ffa500", "Orange")])
    code_correction = SelectField('Error Correction', choices=[("H", "Error Correction"),
                                                               ("H", "H"),
                                                               ("L", "L"),
                                                               ("M", "M"),
                                                               ("Q", "Q")])
    code_image = StringField('Image URL')
    generate_code = SubmitField('Generate QR Code')
