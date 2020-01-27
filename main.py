import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import SignUpForm
from flask_pymongo import PyMongo

os.path("env.py")

import env

if os.path.exists("env.py")
    import env



app = Flask(__name__)
Bootstrap(app)

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI') 
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

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
    app.run(debug=False)
    