import os
from os import path
from flask import Flask, render_template, redirect, url_for, request
import os
from os import path

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/films')
def films():
    return render_template("films.html")


@app.route('/tv')
def tv():
    return render_template("tv.html")


@app.route('/casting')
def casting():
    return render_template("casting.html")


@app.route('/discover')
def discover():
    return render_template("discover.html")


@app.route("/filmdata")
def filmdata():
    return render_template("filmdata.html")


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():


 @app.route('/login', methods=('GET', 'POST'))
  def login():
    error = None
    if request.method == 'POST':
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    error = 'Invalid Credentials. Please try again.'
    else:
    return redirect(url_for('home'))
    return render_template('login.html', error=error)
