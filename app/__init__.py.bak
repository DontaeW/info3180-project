import os
<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, request
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
from .config import Config
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"], supports_credentials=True)

app.config.from_object(Config)
csrf= CSRFProtect(app)
csrf.init_app(app)

db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
=======
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager

app = Flask(__name__)

# Minimal CORS config allowing all origins, methods, and headers for testing
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

app.config.from_object(Config)
csrf = CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads'))
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
<<<<<<< HEAD
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_SECURE'] = True
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
from app import views, models

=======
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_SECURE'] = False
app.config['REMEMBER_COOKIE_HTTPONLY'] = True

app.config['SERVER_NAME'] = 'localhost:5001'

@app.before_request
def log_options_requests():
    if request.method == 'OPTIONS':
        app.logger.debug(f"Received OPTIONS request for {request.path}")

@app.after_request
def set_csrf_cookie(response):
    response.set_cookie('csrf_token', generate_csrf())
    return response

from app import views, models
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
