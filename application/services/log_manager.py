from config import Config
import json
from time import time
import os


class LogManager:
    """
    Utility for creating and managing
    log entries
    """

    def __init__(self):
        self.path = Config.CRON_LOG_PATH
        self.log = json.loads(self.get_cron_log())

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

    def generate_log(self, key):
        """
        Create a new timestamp with the relevant
        Cron ID in the logs.
        """

        self.log[key] = time()
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

    def get_entry(self, key):
        """ 
        Get the timestamp of a specific log entry
        """

        if key not in self.log:
            self.generate_log(key)
            self.log = json.loads(self.get_cron_log())

        return self.log[key]

    def reset(self):
        """ 
        Delete entries in the log
        """
        return os.remove(self.path)
