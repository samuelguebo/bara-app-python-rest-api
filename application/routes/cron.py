from application.services.aej_cron import AEJCron
import flask
from flask import Blueprint
from flask import Flask, jsonify
from application.services.educarriere_cron import EducarriereCron
from application.services.atoo_cron import AtooCron
from application.services.cron_manager import CronManager

cron_bp = Blueprint('cron_bp', __name__)

@cron_bp.route('/cron')
def index():
    
    page_number_limit = 3
    manager = CronManager()
    manager.add(EducarriereCron(page_number_limit))
    manager.add(AEJCron(page_number_limit))
    manager.add(AtooCron(page_number_limit))
    manager.execute()
    logs = manager.get_log()
    
    return (jsonify(logs), 200)
