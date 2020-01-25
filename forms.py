from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import Form, BooleanField, StringField, validators

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')


class RegistratrionForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])