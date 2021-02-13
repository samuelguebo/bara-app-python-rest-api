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
		details_selector = 'ul.list-group'
		offers_selector = 'ul#myList .box.row'
		offer_nodes = soup.select(offers_selector)
	

		for offer_node in offer_nodes:

			# data mapping
			link = "".join([x['href'] for x in offer_node.select(".text-col h4 a")])
			title = "".join([x.get_text() for x in offer_node.select(".text-col h4 a")])
			desc = "".join([x.get_text() for x in offer_node.select(".text-col .entry-title a")])
			datesRegx = "[0-9]{2}\\/[0-9]{2}\\/[0-9]{4}"
			matches = re.findall(datesRegx, offer_node.get_text())

			if len(matches) > 1:
				pubDate = matches[0]
				expDate = matches[1]

				# Extract additional details: degree, type of offers, etc.
				detailsNodesText = "".join([x.get_text() for x in offer_node.select(details_selector)])

				# build entities
				offer = Offer(link, title, desc, pubDate, expDate)
				offer.degrees = self.extractDegrees(detailsNodesText)
				offer.tags.append(Tag("HEALTH"))
				#offer.tags = self.predictTags(link)
				# offer.set_type(self.extractType(detailsNodesText))
				offer.set_type("CDD")
				offer.set_satus("PENDING")

				# save to database
				dao = OfferDao(db)
				dao.create(offer)