from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm)


username = StringField('Username', validators=[DataRequired()])
password = PasswordField('Password', validators=[DataRequired()])
submit = SubmitField('Login')

class SignUpForm(FlaskForm)

username = StringField('Username', validators=[DataRequired()])
password = PasswordField('Password', validators=[DataRequired()])
password_validate = PasswordField(
     'Validate Password', validators=[DataRequired(), EqualTo('password', message='Passwords must be identical.')])
    submit = SubmitField('Register')
)