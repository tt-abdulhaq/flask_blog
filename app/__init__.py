# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Ensure this import is correct

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
