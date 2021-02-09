# -*- coding: utf-8 -*-
# This project is the backend API of a Barra
# a mobile application featuring job offers
#
# Contributors: Samuel Guebo
# Licence: MIT

from flask import Flask
from routes.home import home
from cron.educarriere import educarriere
from flask_crontab import Crontab

app = Flask(__name__)
app.register_blueprint(home)

@crontab.job(minute="2")
def scheduled_job():
    print('This is error output', file=sys.stderr)
    print('This is standard output', file=sys.stdout)

'''
@app.context_processor
def inject_user():
    """Injecting variables in all templates"""
    title = app.config['TITLE']
    description = app.config['DESCRIPTION']
    
    return dict(title=title, description=description)

'''