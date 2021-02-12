from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from .routes import home
from .routes import test
from .routes import cron

# Globally accessible libraries
db = SQLAlchemy()

def create_app(register_blueprints=True):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
        if register_blueprints:
            app.register_blueprint(test.test_bp)
            app.register_blueprint(home.home_bp)
            app.register_blueprint(cron.cron_bp)

    return app
