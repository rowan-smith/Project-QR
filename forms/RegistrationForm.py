from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(2, 30)])
    # first_name = StringField('First Name', validators=[DataRequired(), Length(2, 15)])
    # last_name = StringField('Last Name', validators=[DataRequired(), Length(2, 25)])
    username = StringField('Username', validators=[DataRequired(), Length(3, 25)])
    email = StringField('JCU Email', validators=[DataRequired(), Email(), Length(6, 45)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 20)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Remember Me')
    register = SubmitField('Sign Up')
