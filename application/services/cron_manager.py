import os 
from .. import create_app
import json
from config import Config
from time import time
from datetime import datetime

class CronManager():
    """
    Helper class for triggering cron operations. It avoids 
    unecessary operations by relying on a log file
    which contains ID and timestamp of recently run
    cron operations
    """

    def __init__(self):
        """
        Default constructor with will initiate
        some varibales and make them available
        to the class methods.
        """
        self = self
        self.path = Config.CRON_LOG_PATH
        self.log = json.loads(self.get_cron_log())
        self.tasks = []
    
    def get_latest_cron(self, cron):
        """ 
        Get the timestamp of the latest cron operation
        which was ran for a specific Cron object.
        """
        
        if cron.ID not in self.log:
            self.generate_log(cron)
            self.log = json.loads(self.get_cron_log())
        
        return self.log[cron.ID]

    def get_cron_log(self):
        """
        Read the Log file, a JSON file where cron operations
        are logged for caching purpose
        """
        
        content = ""
        if not os.path.exists(self.path):
            self.update_cron_log({})
        with open(self.path) as f:
            content = f.read()
        
        return content
    
    def generate_log(self, cron):
        """
        Create a new timestamp with the relevant
        Cron ID in the logs.
        """
        
        self.log[cron.ID] = time()
        self.update_cron_log(self.log)
        
        return True

    def update_cron_log(self, log):
        """
        Overwrite existing log file by replacing
        it with a newer version

        :param log: a dictionary containing the 
                    new cron operations log.  
        """
        
        log = json.dumps(log)
        with open(self.path, 'w+') as f:
            f.write(log)
        
        return True

    
    def add(self, cron):
        """
        Build and array of cron operations

        :param cron: a Cron object or of its children
        """
        self.tasks.append(cron)

    
    def run_all(self):
        """
        Process all cron operations in a sequential batch. 
        TODO: explore asyncronicity
        """
        for cron in self.tasks:
            self.run(cron)

    def reset(self):
        """
        Reset tasks list
        """
        self.tasks = []

    def run(self, cron):

        """ 
        Process the Cron task if the time lapse since
        the latest operation exceed the cache_delay

        :param cache_delay: Time lapse since last run
                            in hours
        """
        
        # run anyway if its is the first time
        if cron.ID not in self.log:
            self.generate_log(cron)
            cron.run()
            return True

        latest_time_stamp = datetime.fromtimestamp(self.get_latest_cron(cron))
        now = datetime.fromtimestamp(time())

        # Difference in hours
        lapsed_time = (now - latest_time_stamp).seconds / 3600
        
        # If last cron operation happened n hours ago
        if cron.CACHE_DELAY < lapsed_time:
            cron.run()
            self.generate_log(cron)
            return True
        