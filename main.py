import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from flask_bcrypt import Bcrypt
from os import path
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI') 
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

    

if path.exists("env.py"):
   import env

app = Flask(__name__)
print(os.environ.get('MONGO_URI'))


mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('pages/index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
   users = mongo.db.users
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.uctcnow()
    
    user_id = users.insert({
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email,
        'password' : password,
        'created' : created,
    })
   
   new_user = users.find_one({'_id' : user_id})

   result = {'email' : new_user['email'] + 'registered'}

   return jsonify({'result' : result})




@app.route('/login', methods=['GET', 'POST'])
def login():
    

    if form.validate_on_submit():


    return render_template('pages/login.html', form=form)







    



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
    