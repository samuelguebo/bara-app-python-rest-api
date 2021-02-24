from flask import Blueprint
from flask import jsonify
from config import Config
from application.services.aej_cron import AEJCron
from application.services.atoo_cron import AtooCron
from application.services.cleanup_cron import CleanupCron
from application.services.cron_manager import CronManager
from application.services.educarriere_cron import EducarriereCron

cron_bp = Blueprint('cron_bp', __name__)

@cron_bp.route('/')
def index():
    
    page_number_limit = Config.PAGE_NUMBER_LIMIT
    manager = CronManager()
    manager.add(AEJCron(page_number_limit))
    manager.add(EducarriereCron(page_number_limit))
    manager.add(AtooCron(page_number_limit))
    manager.add(CleanupCron())
    manager.execute()
    logs = manager.get_logs()
    
    return (jsonify(logs), 200)
