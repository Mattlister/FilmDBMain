import os
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def index():

    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('pages/index.html', films=mongo.db.films.find())


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == "POST":
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                flash(f'Thank you, you are now logged in')
                return redirect(url_for('index'))

            else:
                flash(f'Password Incorrect. Please try again', 'danger')
                return redirect(url_for('login'))

        else:
            flash(f'No matching username')
        return redirect(url_for('login'))
    return render_template('pages/login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('pages/register.html')


@app.route("/createmovie", methods=['POST', 'GET'])
def createmovie():
    if request.method == "POST":
        film_data = mongo.db.films
        print(film_data)
        film_data.insert_one(request.form.to_dict())
        return render_template("pages/createmovie.html")

    return render_template("pages/createmovie.html")


@app.route("/createtv", methods=['GET', 'POST'])
def createtv():
    if request.method == "POST":
        film_data = mongo.db.TVData
        print(mongo.db.TVData)
        film_data.insert_one(request.form.to_dict())
        return render_template("pages/createtv.html")

    return render_template("pages/createtv.html")


@app.route("/films")
def films():

    return render_template("pages/films.html")


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