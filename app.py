import os
import datetime
from os import path
from flask import Flask, render_template, redirect, request, url_for, session, \
    flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from forms import LoginForm, RegisterForm, CreateWorkoutForm, EditWorkoutForm, \
    DeleteForm

if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value generated via secrets python module.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
users = mongo.db.users
get_workouts = mongo.db.workouts


@app.route('/')
@app.route('/index')
def index():
    """Landing page render"""
    return render_template('index.html')


@app.route('/fundamentals')
def show_fundamentals():
    """Show user fundamentals from MongoDB documents stored in
    'fundamental_movements' db."""
    return render_template('fundamentals.html',
                           fundamentals=mongo.db.fundamental_movements.find())


@app.route('/public-workouts')
def show_public_workouts():
    """Show workout documents that have the public_workout key value set to
    true on workout creation by logged in user, by utilising if statements in
    the 'public-workouts.html' to check for the value in a for loop."""
    return render_template('public-workouts.html',
                           workouts=mongo.db.workouts.find())


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User Login. If Username not found in MongoDB db 'users', flash message
    and redirect user to try again on Login page. If password entered
    incorrect, flash relevant message and redirect to Login."""
    login_form = LoginForm()

    if login_form.validate_on_submit():
        found_username = users.find_one({'username': request.form['username']})

        if found_username:
            if bcrypt.check_password_hash(found_username['password'],
                                          request.form.get('password').encode(
                                              'utf-8')):
                session['username'] = request.form.get('username')
                session['logged-in'] = True
                return redirect(url_for('my_workouts'))

            flash(f'Password incorrect. Please try again.', 'danger')
            return redirect(url_for('login'))

        flash(f'Username not found. Please try again.', 'danger')
        return redirect(url_for('login'))

    return render_template('login.html', title='Login', form=login_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """User Registration. If Username is not taken and stored in MongoDB db
    'users'. Hashing passwords using Bcrypt credit to Corey Schafer tutorial
    on Youtube, (link in README). Learning aspects altered to suit this
    application. If username is already taken message flashed to user
    detailing same."""
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        found_username = users.find_one({'username': request.form['username']})

        if not found_username:

            hashed_pw = bcrypt.generate_password_hash(
                request.form['password']).decode('utf-8')
            users.insert_one({'username': register_form.username.data,
                              'password': hashed_pw})
            session['username'] = request.form.get('username')
            return redirect(url_for('index'))
        else:
            flash(f'Duplicate username detected. Please try again', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html', title='Register',
                           form=register_form)


@app.route('/logout')
def logout():
    """Logout user by clearing the session cache & redirect with flash
    message to index."""
    session.clear()
    flash(f'Thank you for using Oly-Track. See you soon.', 'primary')
    return redirect(url_for('index'))


@app.route('/create-workout', methods=['GET', 'POST'])
def create_workout():
    """Allow logged in user to create workout. Username auto-populated on
    creation based on session['username'] value. Date is auto-populated
    on creation and stored as date in MongoDB Collection db 'workouts'.
    Location and Focus fields are dropdowns and values therein are set via db
    variables below. Credit to Tim_CI tutor for assisting in fixing my
    error: where I needed to add the location dropdown values alongside the
    focus dropdown values. (link in README)"""
    create_workout_form = CreateWorkoutForm()

    if request.method == 'POST':
        get_workouts.insert_one({
            'username': session['username'],
            'date': datetime.datetime.utcnow().strftime('%H:%M:%S - %d/%m/%Y'),
            'location_name': create_workout_form.location_name.data,
            'focus_name': create_workout_form.focus_name.data,
            'part_a': create_workout_form.part_a.data,
            'part_b': create_workout_form.part_b.data,
            'part_c': create_workout_form.part_c.data,
            'accessory': create_workout_form.accessory.data,
            'additional_info': create_workout_form.additional_info.data,
            'coach_notes': create_workout_form.coach_notes.data,
            'public_workout': create_workout_form.public_workout.data,
        })
        flash(f'Workout added.', 'primary')
        return redirect(url_for('my_workouts', title='Workout Added'))

    # Show dropdown values from collection databases for focus_type &
    # location_name
    focus_type = mongo.db.focus_type.distinct('focus_name')
    create_workout_form.focus_name.choices = [('', 'Please select')] + [
        (focus, focus) for focus in focus_type]
    location_type = mongo.db.location.distinct('location_name')
    create_workout_form.location_name.choices = [('', 'Please select')] + [
        (locale, locale) for locale in location_type]

    return render_template('create-workout.html', form=create_workout_form)


@app.route('/my-workouts')
def my_workouts():
    """View list of workouts ~ only show workouts owned by logged in user via
    statement on template my-workouts.html"""
    return render_template('my-workouts.html',
                           workouts=mongo.db.workouts.find())


@app.route('/workout-view/<workout_id>')
def workout_view(workout_id):
    """View specific workout details full view"""
    my_workout = get_workouts.find_one({'_id': ObjectId(workout_id)})
    return render_template('workout-view.html', workout=my_workout)


@app.route('/edit-workout/<workout_id>', methods=['GET', 'POST'])
def edit_workout(workout_id):
    """Function to post existing workout form and allow user to edit data
    therein. Credit to Edel O' Sullivan for helping me in slack and pointing
    me in the right direction to use 'find_one_or_404' method. (Links in
    README)"""
    edit_workout_form = EditWorkoutForm()
    workout = get_workouts.find_one_or_404({'_id': ObjectId(workout_id)})
    # Show dropdown values from collection databases for focus_type &
    # location_name
    focus_type = mongo.db.focus_type.distinct('focus_name')
    edit_workout_form.focus_name.choices = [('', 'Please select')] + [
        (focus, focus) for focus in focus_type]
    location_type = mongo.db.location.distinct('location_name')
    edit_workout_form.location_name.choices = [('', 'Please select')] + [
        (locale, locale) for locale in location_type]

    if edit_workout_form.validate_on_submit():
        get_workouts.update_one({'_id': ObjectId(workout_id)},
                                {'$set':
                                    {
                                        'location_name':
                                            edit_workout_form.location_name.data,
                                        'focus_name':
                                            edit_workout_form.focus_name.data,
                                        'part_a': edit_workout_form.part_a.data,
                                        'part_b': edit_workout_form.part_b.data,
                                        'part_c': edit_workout_form.part_c.data,
                                        'accessory':
                                            edit_workout_form.accessory.data,
                                        'additional_info':
                                            edit_workout_form.additional_info.data,
                                        'coach_notes':
                                            edit_workout_form.coach_notes.data,
                                        'public_workout':
                                            edit_workout_form.public_workout.data,
                                    }})
        flash(f'Workout updated', 'primary')
        return redirect(url_for('my_workouts', title='Workout updated'))
    # When navigating into /edit_workout/<workout_id> we set the form
    # elements to values set when document created
    elif request.method == 'GET':
        edit_workout_form.location_name.data = workout['location_name']
        edit_workout_form.focus_name.data = workout['focus_name']
        edit_workout_form.part_a.data = workout['part_a']
        edit_workout_form.part_b.data = workout['part_b']
        edit_workout_form.part_c.data = workout['part_c']
        edit_workout_form.accessory.data = workout['accessory']
        edit_workout_form.additional_info.data = workout['additional_info']
        edit_workout_form.coach_notes.data = workout['coach_notes']
        edit_workout_form.public_workout.data = workout['public_workout']
    else:
        flash(f'Something went wrong...Workout not updated.', 'primary')
        return redirect(url_for('my_workouts', title='Error during Update'))

    return render_template('edit-workout.html', workout=workout,
                           form=edit_workout_form)


@app.route('/delete-workout/<workout_id>', methods=['GET', 'POST'])
def delete_workout(workout_id):
    """Allow logged in user to delete workout document they own"""
    my_workout = get_workouts.find_one({'_id': ObjectId(workout_id)})

    delete_workout_form = DeleteForm()
    if request.method == 'POST':
        if session['username'] == request.form.get('username'):
            get_workouts.remove({'_id': ObjectId(workout_id)})
            flash(f'Workout removed.', 'primary')
            return redirect(url_for('my_workouts', title='Workout Removed'))
        flash(f'Wrong username submitted for Delete confirmation', 'primary')
        return redirect(url_for('my_workouts', title='Not your workout.'))

    return render_template('delete-workout.html', workout=my_workout,
                           form=delete_workout_form)


# Error Handling of 404 & 500
@app.errorhandler(404)
def response_404(exception):
    """When 404 is captured display custom 404.html page"""
    return render_template('404.html', exception=exception)


@app.errorhandler(500)
def response_500(exception):
    """When 500 is captured display custom 500.html page"""
    return render_template('500.html', exception=exception)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=os.environ.get('PORT', '5000'),
            debug=False)