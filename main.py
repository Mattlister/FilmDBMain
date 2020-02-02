from os import path
import os
import datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from flask import jsonify
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

print(os.environ.get("MONGO_URI"))


@app.route("/")
@app.route("/index")
def index():
    return render_template("pages/index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    return render_template("pages/signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("pages/login.html")


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