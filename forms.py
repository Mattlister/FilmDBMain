from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, PasswordField, SelectField, BooleanField
from wtforms import Form, BooleanField, StringField, PasswordField, validators


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=12)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password',
                                                                             message='Passwords must be the same.')])

 submit = SubmitField('Signup')                                                                            

class RegistratrionForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password',
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')

    confirm = PasswordField('Repeat Password')
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])

     submit = SubmitField('Register')

     class CreateMovieInfoForm(FlaskForm):
         submit = SubmitField('create')

     class EditMovieInfoForm(FlaskForm):
         submit = SubmitField('Update')

     class DeleteForm(FlaskForm):
        submit = SubmitField('Delete')                                                                             
    