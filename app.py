import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_pymongo import PyMongo
from forms import RegistrationForm, LoginForm
from os import path
if path.exists('env.py'):
    import env


app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for('home'))
    return render_template('pages/register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'mdlister24@hotmail.com' and\
         form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, please check username and\
             password', 'danger')
        return render_template('pages/login.html', title='Login', form=form)
    return render_template('pages/login.html', title='Login', form=form)


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
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=os.environ.get('PORT', '5000'),
            debug=True)