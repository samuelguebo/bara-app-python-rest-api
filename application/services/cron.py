import re
from config import Config

class Cron:
    ID = 'default'
    
    def __init__(self):
        self = self

    def extractWithRegex(self, text, regexPattern):
        matches = []
        matches = [match for match in re.findall(regexPattern, text)]

        # Grab only first item
        if len(matches) == 1:
            return matches[0];
        
        return matches

    def extractDegrees(self, text):
        return self.extractWithRegex(text.upper(), Config.DEGREE_REGEX)

    def extractType(self, text):
        return self.extractWithRegex(text.upper(), Config.TYPE_REGEX)