from flask_wtf import FlaskForm
from wtforms import StringFiled, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringFiled('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')
