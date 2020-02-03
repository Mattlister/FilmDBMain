import os
from flask import Flask
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
import PyMongo
from flask_bcrypt import bcrypt
import Bcrypt

if path.exists("env.py"):

    import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
users = mongo.db.users

print(os.environ.get("MONGO_URI"))


@app.route("/")
@app.route("/index")
def index():
    return render_template("pages/index.html")

# Login


@app.route('/login', methods=['GET'])
def login():
    for now
    if 'user' in session:
        user_in_db = users_collection.find_one({
         "username": session['user']
        })
    if user_in_db:
        # If so redirect user to his profile

   else:
    flash("You are logged in already!")
return redirect(url_for('profile', user = user_in_db['username']))
else:
return render_template("login.html")

# Check user login details
@app.route('/user_auth', methods = ['POST'])
def user_auth():
  form = request.form.to_dict()
user_in_db = users_collection.find_one({
  "username": form['username']
})# Check db
for user
if user_in_db:

  if check_password_hash(ser_in_db['password'], form['user_password']):
  session['user'] = form['username']
if session['user'] == "admin":
  return redirect(url_for('admin'))
else :
  flash("Yeah baby!")
return redirect(url_for('profile', user = user_in_db['username']))

else :
  flash("We hate to say this but either your username or password is wrong!")
return redirect(url_for('login'))
else :
  flash("You must be a chosen one!")
return redirect(url_for('register'))

# Sign up
@app.route('/register', methods = ['GET', 'POST'])
def register(): #Check
if user is not logged in already
if 'user' in session:
  flash('You know this place!')
return redirect(url_for('index'))
if request.method == 'POST':
  form = request.form.to_dict()# Check
if the password and password1 actualy match
if form['user_password'] == form['user_password1']: #If so
try to find the user in db
user = users_collection.find_one({
  "username": form['username']
})
if user:
  flash(f "{form['username']} already exists!")
return redirect(url_for('register'))# If user does not exist register new user
else :#password
hash_pass = generate_password_hash(form['user_password'])# Create new user with password
users_collection.insert_one({
  'username': form['username'],
  'email': form['email'],
  'password': hash_pass
})# Check
if user is actualy saved
user_in_db = users_collection.find_one({
  "username": form['username']
})
if user_in_db: #Log user in (add to session)
session['user'] = user_in_db['username']
return redirect(url_for('profile', user = user_in_db['username']))
else :
  flash("Dude, there was a problem signing in")
return redirect(url_for('register'))

else :
  flash("Passwords don't match, you shall not pass!")
return redirect(url_for('register'))

return render_template("register.html")

# Log out
@app.route('/logout')
def logout(): #Clear the session
session.clear()
flash('You were logged out!')
return redirect(url_for('index'))






@app.route("/films")
def films():
  return render_template("pages/films.html")

@app.route("/tv")
def tv():
  return render_template("pages/tv.html")

@app.route("/casting")
def casting():
  return render_template("pages/casting.html")

@app.route("/contact")
def contact():
  return render_template("pages/contact.html")

# 404 error page
@app.errorhandler(404)
def page_not_found(e):
  return render_template("pages/404.html"), 404

if __name__ == "__main__":
  app.run(debug = False)