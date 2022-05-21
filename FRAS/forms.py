from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[data_required(), Length(min=2, max=20)])
    email = StringField('Email', validators=[data_required(), Email()])
    password = StringField('Password', validators=[data_required()])
    confirm_password = StringField('Confirm Password', validators=[data_required(), EqualTo('password')])
    submit = SubmitField('Sign Up') 

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[data_required(), Email()])
    password = StringField('Password', validators=[data_required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login') 

