import flask
from flask import Blueprint
from flask import Flask, jsonify
import os
import re
import json
import timeago
from datetime import datetime
from config import Config

app = Flask(__name__)
cron_bp = Blueprint('cron_bp', __name__)

@cron_bp.route('/cron')
def index():
    from ..services.cron import Cron
    from ..services.educarriere_cron import EducarriereCron
    from ..services.atoo_cron import AtooCron
    from ..services.cron_manager import CronManager
    
    manager = CronManager()
    manager.add(EducarriereCron())
    manager.add(AtooCron())
    manager.run_all()
    data = ['{} was updated {}.'.format(cron.ID, timeago.format(manager.get_latest_cron(cron))) for cron in manager.tasks]
    
    return (jsonify(data), 200)
