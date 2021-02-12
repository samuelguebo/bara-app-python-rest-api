import os 
from .. import create_app
import json
from config import Config

class CronManager:
    
    def __init__(self):
        self = self
    
    def get_latest_cron(self, cron_id):
        content = self.get_cron_log(Config.CRON_LOG_PATH)
        content = json.loads(content)
        latest_cron = content[cron_id]
    
    def get_cron_log(self, path):
        
        content = ""
        if not os.path.exists(path):
            self.write_cron_log(path, {})
        
        with open(path) as f:
            content = f.read()
        return content

    def write_cron_log(self, path, logs):
        logs = json.dumps(logs)
        with open(path, 'w+') as f:
            f.write(logs)