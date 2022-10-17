# imports
from FirstSight.funcs import save_picture
from FirstSight import app, db, bcrypt
from FirstSight.models import Users
from FirstSight.forms import *
from flask import abort, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET', 'POST'])
def home_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))

    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home_page'))

        else:
            flash("Login Unsuccessful. Please Check The Email And Password", 'danger')

    return render_template("home_page.html", form=form)



@app.route("/register", methods=['POST', 'GET'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.profile_image.data:
            picture_file = save_picture(form.profile_image.data)
            current_user.image_file = picture_file

        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = Users(name = form.name.data, email = form.email.data, age = form.age.data, team = form.team.data, gender = form.gender.data, date_of_birth = form.date_of_birth.data, hobbies = form.hobbies.data, friends_opinion = form.friends_opinion.data, one_word_about_user = form.one_word_about_user.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('בהצלחה לך מצטרף חדש', 'success')
        return redirect(url_for('home_page'))
    else:
        return render_template("register.html", form=form)

@app.route("/pickup_lines")
def pickup_lines_page():
    return render_template("pick_up_lines.html")

@app.route("/Friends", methods=['POST', 'GET'])
def friends():

    if request.method == 'POST':
        friend_name = request.form['name']
        new_friend = Users(username=friend_name)
        try:
            db.session.add(new_friend)
            db.session.commit()
            return redirect('/Friends')
        except:
            return 'ERRRORRRRRORORORORORROORORORORRRRRORORORRRORORORORORORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR'

    else:
        friends = Users.query.order_by(Users.date_created)
        return render_template('Friends.html', friends=friends)

@app.route("/login", methods=['GET', 'POST'])
def login():
    pass

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/user-info")
# @login_required
def user_info():
    return render_template("user-info.html")

