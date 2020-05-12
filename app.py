import os
from flask import Flask, render_template, url_for, request, session, \
    redirect, flash
from data import AllMovies
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm, CreateMovieForm, DeleteMovieForm

if os.path.exists('env.py'):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Secret Key value
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


allmovies = AllMovies()

mongo = PyMongo(app)
users = mongo.db.users
bcrypt = Bcrypt(app)
get_films = mongo.db.films


@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        flash(f'You are logged in as ' + session['username'], 'success')

    return render_template('pages/index.html', films=mongo.db.films.find())

# Register New User
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        users = mongo.db.users
        found_username = users.find_one({'username': request.form['username']})

        if found_username is None:
            hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            users.insert({'username': request.form['username'], 'password': hashed_password})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            flash(f'This name already exists. Please use a different name', 'danger')
        return redirect(url_for('index'))
    return render_template('pages/register.html', title='Register', form=form)


# Login User
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if 'username' in session:
            flash("You crazy kid, you're already logged in", 'danger')
        else:
            users = mongo.db.users
            found_username = users.find_one({'username': request.form['username']})

            # Check if hashed password in mongo.db.users is correct
            if found_username:
                if bcrypt.check_password_hash(found_username['password'], (request.form['password']).encode('utf-8')):
                    session['username'] = request.form['username']
                    return redirect(url_for('index'))
                else:
                    flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('pages/login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return render_template('pages/index.html')


# create movie entry

@app.route("/createmovie", methods=['GET', 'POST'])
def createmovie():
    if request.method == "POST":
        film_data = mongo.db.films
        print(film_data)
        film_data.insert_one(request.form.to_dict())

    return render_template("pages/createmovie.html")


# read movie entries

@app.route("/mymovie")
def mymovie():

    return render_template("pages/myreviews.html", reviews=get_films.find())


# update movie entry

@app.route("/editmovie/<movieid>", methods=["GET", "POST"])
def editmovie(movieid):
    if request.method == "POST":
        movie = get_films.find_one_or_404({"_id": ObjectId(movieid)})
        get_films.update_one(movie, {"$set": request.form.to_dict()})

    return render_template("pages/editmovie.html", reviews=get_films.find_one({"_id": ObjectId(movieid)}))


# delete movie entry

@app.route("/deletemovie/<movieid>", methods=["GET", "POST"])
def deletemovie(movieid):
    get_films.delete_one({"_id": ObjectId(movieid)})
    return render_template("pages/deletemovie.html")


# display movie reviews

@app.route("/amovie/<movieid>")
def amovie(movieid):
    review = get_films.find_one({"_id": ObjectId(movieid)})
    print(review)
    return render_template("pages/myreview.html", review=get_films.find_one({"_id": ObjectId(movieid)}))


# search for movies

@app.route("/films")
def films():

    return render_template("pages/films.html")


# 404 error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("pages/404.html"), 404


# 404 error page
@app.errorhandler(500)
def server_not_found(error):
    return render_template("pages/500.html"), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEBUG'))
