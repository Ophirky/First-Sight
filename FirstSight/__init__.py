from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '7fe1c8903139cbfc30ec4e6bb859a4e2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\ophir\\Desktop\\Projects\\Flask-Web\\First-Sight\\FirstSight\\site.db'

flask.current_app = app

bcrypt = Bcrypt(app)

# Init the db #
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from FirstSight import routes
from FirstSight import models

