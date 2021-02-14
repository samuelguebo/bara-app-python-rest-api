import re
from bs4 import BeautifulSoup
import requests
from config import Config

class Cron:
	"""
	Base class for automated operations, a.k.a cron jobs.
	Cron tasks will inherit this class 
	"""
	ID = 'default'

	def __init__(self):
		self = self

	def extractWithRegex(self, text, regexPattern, unique=False):
		"""
		Use a Regex expression to extract certain portions of texts
		
		:param text: Body of text to comb through
		:param regexPattern: Regular expression used for extraction
		"""
		
		matches = []
		matches = [match for match in re.findall(regexPattern, text)]

		# Grab only first item
		if len(matches) == 1 or (len(matches) > 0 and unique):
			return matches[0];
		
		return matches

	def extractContent(self, url, selector):
		"""
		Scan through url to get page content 
		"""

		html_doc = requests.get(url).text
		soup = BeautifulSoup(html_doc, 'html.parser')
		content = ""

		for x in soup.select(selector):
			content += x.get_text()

		return content.replace("\n\n", " ")
    
	def extractDegrees(self, text):
		"""Extract the education level requirements"""
		return self.extractWithRegex(text.upper(), Config.DEGREE_REGEX)

	def extractType(self, text):
		"""Extract the type of job offer"""
		result = self.extractWithRegex(text.upper(), Config.TYPE_REGEX, True)
		if len(result) < 1:
			return Config.DEFAULT_TYPE
		
		return result