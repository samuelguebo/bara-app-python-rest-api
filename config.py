from decouple import config

class Config(object):
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GREETING = config('GREETING')
    TITLE =  config('TITLE')
    DESCRIPTION = config('DESCRIPTION')
    NAMESPACE = config('NAMESPACE')
    DATABASE_URL = config('DATABASE_URL')
    CRON_LOG_PATH = config('CRON_LOG_PATH')