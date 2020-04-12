from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class CreateMovieForm(FlaskForm):
    movie_name = SelectField('Name')
    submit = SubmitField('Create')


class EditMovieForm(FlaskForm):
    movie_name = SelectField('Name')
    submit = SubmitField('Edit')


class DeleteForm(FlaskForm):
    username = StringField('username')
    submit = SubmitField('Delete')
