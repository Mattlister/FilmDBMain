import os
from flask import Flask, render_template, url_for, request, session, \
    redirect, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
users = mongo.db.users
bcrypt = Bcrypt(app)


@app.route('/')
def index():

    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('pages/index.html', films=mongo.db.films.find())


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if 'username' in session:
            flash("You crazy kid, you're already logged in", 'danger')
        else:
            users = mongo.db.users
            found_username = users.find_one({'username': request.form['username']})

            if found_username:
                if bcrypt.check_password_hash(found_username['password'],
                    request.form('password').encode('utf-8')):
                    session['username'] = request.form('username')
                    return redirect(url_for('index'))
                else:
                    flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('pages/login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            users.insert({'username': request.form['username'], 'password': hashed_password})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        flash(f'This name already exists. Please use a different name', 'danger')
        return redirect(url_for('register'))
    return render_template('pages/register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return render_template('pages/index.html')


@app.route("/createmovie", methods=['GET', 'POST'])
def createmovie():
    if request.method == "POST":
        film_data = mongo.db.films
        print(film_data)
        film_data.insert_one(request.form.to_dict())
        return render_template("pages/createmovie.html")

    return render_template("pages/createmovie.html")


@app.route("/edit-movie.html")
def editmovie():
    return render_template("pages/editmovie.html")


@app.route("/delete-movie.html")
def deletemovie():
    return render_template("pages/deletemovie.html")


@app.route("/contact")
def contact():
    return render_template("pages/contact.html")


@app.route("/films")
def films():

    return render_template("pages/films.html")


@app.route("/moviereviews")
def moviereviews():

    return render_template("pages/moviereviews.html")


@app.route("/myreviews.html")
def myreviews():

    return render_template("pages/myreviews.html")

# 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("pages/404.html"), 404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=os.environ.get('PORT', '5000'),
            debug=True)
