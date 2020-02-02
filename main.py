from os import path
import os
from flask import Flask, render_template, redirect, request, url_for,
request
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

if path.exists("env.py"):
      import env # pylint: disable=W0611

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
users = mongo.db.users

# Collections

print(os.environ.get("MONGO_URI"))

@app.route("/")
@app.route("/index")
def index():
    return render_template("pages/index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Check to see if user is already logged in
    if 'user' in session:
        user_in_db = users_collection.find_one({"username":
session['user']})
        if user_in_db:
            # If found, redirect user to their profile
            flash("This is the page you are looking for!")
            return redirect(url_for('profile', user=user_in_db['username']))
    else:
        # Display login page for the user        
    return render_template("pages/login.html")

#Sign up
@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Check if new user
    if 'user' in session:
        flash('You know this place!')
        return redirect(url_for('index'))
    if request.method == 'POST':
        form = request.form.to_dict()
        # Check if passwords match
        if form['user_password'] == form['user_password1']:
            # If successful, find user in db
            user = users_collection.find_one({"username" :
 form['username']})
            if user:
                flash(f"{form['username']} already exists!")
                return redirect(url_for('register'))
                    
    users = mongo.db.users
    first_name = request.get_json()["first_name"]
    last_name = request.get_json()["last_name"]
    email = request.get_json()["email"]
    password = bcrypt.generate_password_hash(request.get_json()["password"]).decode(
        "utf-8"
    )
    created = datetime.utcnow()
    user_id = users.insert(
        {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "created": created,
        }
    )

    new_user = users.find_one({"_id": user_id})

    result = {"email": new_user["email"] + "registered"}

    return jsonify({"result": result})


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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)