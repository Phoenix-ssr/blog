from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
#app.secret_key='safefrff#@#$5tdsfwdf564'
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy(app)
migrate = Migrate(app,db)
from flask_login import LoginManager
login = LoginManager(app)
login.login_view = 'login'
from app import routes,models
