from datetime import datetime, timedelta
from application.models.degree import Degree
from application.models.tag import Tag
from application.models.offer import DeegreeSchema, Offer, TagsSchema
from application.ai.classifier import Classifier
from application.dao.offer_dao import OfferDao
import re
from bs4 import BeautifulSoup
import requests
from config import Config, db

class Cron:
	"""
	Base class for automated operations, a.k.a cron jobs.
	Cron tasks will inherit this class 
	"""
	
	ID = 'default'
	CACHE_DELAY = 12 # twelve hours by default
	DETAILS_SELECTOR = '.detailsOffre > div:not(.content-area)'
	OFFERS_SELECTOR = 'ul#myList .box.row'
	TITLES_SELECTOR = '.text-col h4 a'
	DESC_SELECTOR = '.text-col .entry-title a'
	PENDING = 'PENDING'		

	def __init__(self, page_number=1):
		self.page_number = page_number


	def extract_with_regex(self, text, regexPattern, unique=False):
		"""
		Use a Regex expression to extract certain portions of texts
		
		:param text: Body of text to comb through
		:param regexPattern: Regular expression used for extraction
		"""
		
		matches = []
		matches = [match.replace(' ', '') for match in re.findall(regexPattern, text)]

		# Grab only first item
		if len(matches) == 1 or (len(matches) > 0 and unique):
			return matches[0];
		
		return matches


	def extract_content(self, url, selector):
		"""
		Scan through url to get page content 
		"""

		html_doc = requests.get(url).text
		soup = BeautifulSoup(html_doc, 'html.parser')
		content = ""

		for x in soup.select(selector):
			content += x.get_text()

		return content.replace("\n\n", " ")
    

	def extract_degrees(self, text):
		"""
		Extract the education level requirements
		"""
		
		degrees = self.extract_with_regex(text.upper(), Config.DEGREE_REGEX)
		if isinstance(degrees, list):
			degrees = [Degree(x) for x in set(degrees)]
		else:
			degrees = [Degree(degrees)]
		
		return degrees


	def extract_type(self, text):
		"""
		Extract the type of job offer
		"""
		
		result = self.extract_with_regex(text.upper(), Config.TYPE_REGEX, True)
		if len(result) < 1:
			return Config.DEFAULT_TYPE
		
		return result


	def scrape_home_page(self, url):
		"""
		Comb through url to extract content
		"""

		html_doc = requests.get(url).text
		soup = BeautifulSoup(html_doc, 'html.parser')
		nodes = soup.select(self.OFFERS_SELECTOR)
		
		for node in nodes:

			# Data mapping
			url = "".join([x['href'] for x in node.select(self.TITLES_SELECTOR)])
			title = "".join([x.get_text() for x in node.select(self.TITLES_SELECTOR)])
			desc = "".join([x.get_text() for x in node.select(self.DESC_SELECTOR)])
			dates = self.extract_dates(node.get_text())

			# if empty pub_date is always generated automatically
			pub_date = dates[0]
			exp_date = None
			
			if len(dates) > 1:
				exp_date = dates[1]

			# Check whether we have a valid url
			if len(url) > 10: 
				
				# Extract additional details: degree, type of offers, etc.
				# print('{} {} {}'.format(url, title, desc, pub_date, exp_date))
				offer = Offer(url, title, desc, pub_date, exp_date)
				offer.content = self.extract_content(url, self.DETAILS_SELECTOR)
				offer.degrees = self.extract_degrees(offer.content)
				offer.set_type(self.extract_type(offer.content))
				offer.set_satus(self.PENDING)
				offer.tags = [Tag(x) for x in Classifier().predict_category(offer)]
				if len(offer.tags) > 0:
					offer.set_image(offer.tags)
				
				# Save to database
				dao = OfferDao(db)
				dao.create(offer)


	def extract_dates(self, text):
		"""
		Extract dates from the content
		of a job offer.
		"""
		datesRegx = "[0-9]{2}[\/\s]?[0-9]{2}[\/\s]?[0-9]{4}"
		dates = re.findall(datesRegx, text)
		
		if len(dates) < 1:	
			# Default pub_date is now, and expiration is 2 weeks away
			dates = [datetime.now().strftime('%d/%m/%Y'),
						(datetime.now() + timedelta(days=14)).strftime('%d/%m/%Y')]
		
		return dates