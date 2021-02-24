from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from config import db
from config import migrate
from .routes import home
from .routes import cron
from .routes import offer

def create_app(register_blueprints=True):
	app = Flask(__name__, instance_relative_config=True,
			static_url_path='', 
			static_folder=Config.ROOT_FOLDER + '/static',
			template_folder=Config.ROOT_FOLDER + '/templates')

	app.config.from_object(Config)

	with app.app_context():
		
		if register_blueprints:
			app.register_blueprint(home.home_bp)
			app.register_blueprint(cron.cron_bp, url_prefix='/cron')
			app.register_blueprint(offer.offer_bp, url_prefix='/offer')

	return app
