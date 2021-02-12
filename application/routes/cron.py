import flask
from flask import Blueprint
from flask import Flask
import os
import re
import json
from time import time
from config import Config

app = Flask(__name__)
cron_bp = Blueprint('cron_bp', __name__)

@cron_bp.route('/cron')
def index():
    from ..services.cron_manager import CronManager
    manager = CronManager()
    path = Config.CRON_LOG_PATH
    log = {}
    log['educarriere'] = time()
    data = json.loads(manager.get_cron_log(path))
    
    # update all logs
    for k in log.keys():
        data[k] = log[k]
        

    manager.write_cron_log(path, data)
    return (data, 200)
