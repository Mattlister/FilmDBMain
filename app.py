import os
from flask import Flask, render_template, url_for
from forms import RegistratrionForm, LoginForm
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

bcrypt = Bcrypt(app)
mongo = PyMongo(app)

posts = [
    {
        'user': 'Matthew Lister',
        'title': 'First movie entry',
        'content': 'Empire Sucks',
        'date_posted': 'February 4, 2020'
    },
    {
        'user': 'Samantha Lister',
        'title': 'First TV entry',
        'content': 'Loving Suits',
        'date_posted': 'February 5, 2020'
    }
]

app = Flask(__name__)
print(os.environ.get('MONGO_URI'))


@app.route('/')
@app.route('/index')
def index():
    return render_template('pages/index.html')


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistratrionForm()
    return render_template('pages/register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('pages/login.html', title='Login', form=form)










"""

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
    app.run(debug=True)
    """
