from FirstSight import db
from datetime import datetime
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    hobbies = db.Column(db.Text, nullable=False)
    friends_opinion = db.Column(db.String(100), nullable=False)
    one_word_about_user = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False, unique=False)
    profile_image = db.Column(db.String(20), nullable=False, default="default.jpg")

    matches = db.Column(db.Text, unique=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User(name={self.name}, id={self.id}, mail={self.mail})"