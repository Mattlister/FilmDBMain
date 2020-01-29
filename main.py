import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from os import path
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

if path.exists("env.py"):
   import env

app = Flask(__name__)
print(os.environ.get('MONGO_URI'))

app.config['MONGO_URI'] = os.environ.get('MONGO_URI') 
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('pages/index.html')

@app.route('/login')
def login():
    form = LoginForm()


    return render_template('pages/login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    return render_template('pages/signup.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard')    

@app.route('/films')
def films():
    return render_template('pages/films.html')


@app.route('/tv')
def tv():
    return render_template('pages/tv.html')


@app.route('/casting')
def casting():
    return render_template('pages/casting.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')


  

# 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

if __name__ == "__main__":
    app.run(debug=False)
    