from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired("Please enter your name.")])
    username = StringField('Username', validators=[InputRequired("Please enter your username.")])
    email = StringField('Email', validators=[InputRequired("Please enter your email.")])
    password = PasswordField('Password', validators=[InputRequired("Please enter your password.")])
    remember_me = BooleanField('Remember Me')
    register = SubmitField('Sign Up')
