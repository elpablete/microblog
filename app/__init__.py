from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create Flask app
app = Flask(__name__)

# Apply configuration
app.config.from_object(Config)

# Add flask extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login' #name of the login view (the name you would use in a url_for())

from app import routes, models
