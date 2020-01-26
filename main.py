import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from forms import SignUpForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    user_collection = mongo.db.users
    user_collection.insert({'name : Matthew'})
    return '<h1>Added a User!</h1>'

app = Flask(__name__)
app.comfig["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config['MONDOG_DBNAME'] = os.environ.get("MONGO_DBNAME")    
app.config['SECRET_KEY'] = os.environ.get["SECRET_KEY"]

mongo = PyMongo(app)
users = mongo.db.users

app = Flask(__name__)
Bootstrap(app)



@app.route('/index')
def index():
    return render_template('pages/index.html')


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


@app.route('/login')
def login():
    return render_template('pages/login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    return render_template('pages/signup.html', form=form)  



if __name__ == "__main__":
    app.run(debug=True)