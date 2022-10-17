from logging import PlaceHolder
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from FirstSight.models import Users

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=200)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_con = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    age = IntegerField('Age', validators=[DataRequired()])
    team = StringField('Team', validators=[DataRequired(), Length(min=2, max=200)])
    gender = StringField('Gender', validators=[DataRequired()])
    date_of_birth = DateField('Birthday', validators=[DataRequired()])
    hobbies = StringField('Hobbies', validators=[DataRequired()])
    one_word_about_user = StringField("One word about you", validators=[DataRequired(), Length(min=2, max=50)])
    friends_opinion = StringField("Friends Opinion Of You", validators=[DataRequired(), Length(min=2, max=100)])
    profile_image = FileField("Update Profile Picture", validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('הרשם')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken')

    def validate_email(self, email):
        email = Users.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('An account with this email already exists!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('הכנס')