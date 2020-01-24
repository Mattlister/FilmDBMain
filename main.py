import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
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


@app.route('/login')
def signup(): 
    return render_template('pages/login.html')



if __name__ == "__main__":
    app.run(debug=True)