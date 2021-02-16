from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from config import db
from config import migrate
from .routes import home
from .routes import test
from .routes import cron
from .routes import offer

def create_app(register_blueprints=True):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        db.create_all()
        
        if register_blueprints:
            app.register_blueprint(test.test_bp)
            app.register_blueprint(home.home_bp)
            app.register_blueprint(cron.cron_bp)
            app.register_blueprint(offer.offer_bp, url_prefix='/offer')

    return app
