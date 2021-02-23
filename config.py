import os
from decouple import config
from flask_executor import Executor
from flask_migrate import Migrate
from flask import Flask
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
	CLEANUP_DEADLINE = config('CLEANUP_DEADLINE')

    
class TestConfiguration():
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Async
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Globally accessible libraries
migrate = Migrate()
app = Flask(__name__)
app.config.from_object(Config)
ma = Marshmallow(app)
db = SessionLocal()
executor = Executor(app)
