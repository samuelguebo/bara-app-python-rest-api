import flask
from flask import Blueprint
from flask import Flask
import os
import re
import json
from time import time
from datetime import datetime
from config import Config

app = Flask(__name__)
cron_bp = Blueprint('cron_bp', __name__)

@cron_bp.route('/cron')
def index():
    from ..services.cron import Cron
    from ..services.educarriere_cron import EducarriereCron
    from ..services.cron_manager import CronManager
    cron = EducarriereCron()
    manager = CronManager(cron)
    manager.run(3)
    data = datetime.fromtimestamp(manager.get_latest_cron())
    return (str(data), 200)
