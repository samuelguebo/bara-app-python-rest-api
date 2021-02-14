from application.ai.classifier import Classifier
from config import Config
import sys
from bs4 import BeautifulSoup
import json
import requests
import re
import sys
from flask import Flask
from requests import models
from ..models.offer import Offer
from ..models.tag import Tag
from ..models.degree import Degree
from ..dao.offer_dao import OfferDao
from .cron import Cron
from .. import db

class EducarriereCron(Cron):
	ID   		= "EDUCARRIERE"
	ROOT_URL    = "https://emploi.educarriere.ci/"
	URL_LIST    = ROOT_URL + "nos-offres"

	def run(self):
		for i in range(1):
			url = '{}?page1={}'.format(self.URL_LIST, i)
			self.scrape_home_page(url)

	def scrape_home_page(self, url_list):
		html_doc = requests.get(url_list).text
		soup = BeautifulSoup(html_doc, 'html.parser')
		details_selector = '.detailsOffre > div:not(.content-area)'
		offers_selector = 'ul#myList .box.row'
		offer_nodes = soup.select(offers_selector)
	

		for offer_node in offer_nodes[:5]:

			# Data mapping
			url = "".join([x['href'] for x in offer_node.select(".text-col h4 a")])
			title = "".join([x.get_text() for x in offer_node.select(".text-col h4 a")])
			desc = "".join([x.get_text() for x in offer_node.select(".text-col .entry-title a")])
			datesRegx = "[0-9]{2}\\/[0-9]{2}\\/[0-9]{4}"
			matches = re.findall(datesRegx, offer_node.get_text())

			if len(matches) > 1:
				pubDate = matches[0]
				expDate = matches[1]

				# Extract additional details: degree, type of offers, etc.
				offer = Offer(url, title, desc, pubDate, expDate)
				offer.content = self.extractContent(url, details_selector)
				offer.degrees = [Degree(x) for x in set(self.extractDegrees(offer.content))]
				offer.set_type(self.extractType(offer.content))

				offer.tags = [Tag(x) for x in Classifier().predict_category(offer)]
				
				# Save to database
				dao = OfferDao(db)
				dao.create(offer)
