from application.services.aej_cron import AEJCron
import flask
from flask import Blueprint
from flask import Flask, jsonify
import timeago

cron_bp = Blueprint('cron_bp', __name__)

@cron_bp.route('/cron')
def index():
    from ..services.educarriere_cron import EducarriereCron
    from ..services.atoo_cron import AtooCron
    from ..services.cron_manager import CronManager
    
    manager = CronManager()
    manager.add(EducarriereCron())
    manager.add(AtooCron())
    manager.add(AEJCron())
    manager.execute()
    data = ['{} was updated {}.'.format(cron.ID, timeago.format(manager.get_latest_cron(cron))) for cron in manager.tasks]
    
    return (jsonify(data), 200)
