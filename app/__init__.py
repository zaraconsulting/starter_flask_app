from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        # from . import models
        
        from app.blueprints.main import bp as main
        app.register_blueprint(main, url_prefix='/')

    return app