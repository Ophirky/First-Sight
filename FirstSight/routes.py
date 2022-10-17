# imports
from FirstSight.funcs import save_picture
from FirstSight import app, db, bcrypt
from FirstSight.models import Users
from FirstSight.forms import *
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET', 'POST'])
def home_page():
    if current_user.is_authenticated:
        current_user_id = current_user.id
        return redirect(f"user/{str(current_user_id)}")

    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)


            print("Log in successful")
            flash("Login successful.", 'success')

            return redirect(url_for('home_page'))



        else:
            flash("Login Unsuccessful. Please Check The Email And Password", 'warning')
            print("Log in not successful")


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

@app.route("/logout")
@login_required
def logout_page():
    logout_user()
    flash('Logged Out Successfully', 'success')
    return redirect(url_for('home_page'))

@app.route("/tests")
def tests_p():
    return render_template("tests.html")


@app.route("/user/<user_id>")
def user_info_page(user_id):
    return f"the user id is {user_id}"