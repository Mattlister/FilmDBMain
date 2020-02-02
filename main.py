from os import path
import os, datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from flask import jsonify
from wtforms import StringField, PasswordField, BooleanField
from flask_bcrypt import Bcrypt
from wtforms.validators import InputRequired, Email, Length

if path.exists("env.py"):
    import env # pylint: disable=W0611

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


bcrypt = Bcrypt(app)
mongo = PyMongo(app)


app = Flask(__name__)
print(os.environ.get("MONGO_URI"))


@app.route("/")
@app.route("/index")
def index():
    return render_template("pages/index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    users = mongo.db.users
    first_name = request.get_json()["first_name"]
    last_name = request.get_json()["last_name"]
    email = request.get_json()["email"]
    password = bcrypt.generate_password_hash(request.get_json()["password"]).decode(
        "utf-8"
    )
    created = datetime.uctcnow()

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


@app.route("/login", methods=["GET", "POST"])
def login():
    users = mongo.db.users
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    result = ""

    response = users.find_one({"email": email})

    if response:
        if bcrypt.check_password_hash(response["password"], password):
            access_token = create_access_token(
                identity={
                    "first_name": response["first_name"],
                    "last_name": response["last_name"],
                    "email": response["email"],
                }
            )
            result = jsonify({"token": access_token})
        else:
            result = jsonify({"error": "Invalid username and password"})
    else:
        result = jsonify({"result": "No results found"})
    return result


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
    app.run(debug=True)
