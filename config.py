from decouple import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask_marshmallow import Marshmallow

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
ma = Marshmallow(app)

class Config(object):
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GREETING = config('GREETING')
    TITLE =  config('TITLE')
    DESCRIPTION = config('DESCRIPTION')
    DATABASE_URL = config('DATABASE_URL')
    CRON_LOG_PATH = config('CRON_LOG_PATH')
    DEGREE_REGEX = config('DEGREE_REGEX')
    TYPE_REGEX = config('TYPE_REGEX')
    DEFAULT_TYPE = config('DEFAULT_TYPE')
    ROOT_FOLDER = config('ROOT_FOLDER')

    
