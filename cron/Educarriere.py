import sys
from bs4 import BeautifulSoup
import json
import requests
import re
import sys

class Educarriere():
	ROOT_URL        = "https://emploi.educarriere.ci/"
	PROVIDER_NAME   = "EDUCARRIERE"
	URL_LIST      	= ROOT_URL + "nos-offres"

	def __init__(self):
		self = self

	def scrape_all_pages(self):
		for i in range(1):
			url = '{}?page1={}'.format(self.URL_LIST, i)
			self.scrape_home_page(url)

	def scrape_home_page(self, url_list):
		html_doc = requests.get(url_list).text
		soup = BeautifulSoup(html_doc, 'html.parser')
		offerNodes = soup.select("ul#myList .box.row")

		# print(offerNodes)
		for offerNode in offerNodes:

			# data mapping
			link = "".join([x['href'] for x in offerNode.select(".text-col h4 a")])
			title = "".join([x.get_text() for x in offerNode.select(".text-col h4 a")])
			desc = "".join([x.get_text() for x in offerNode.select(".text-col .entry-title a")])
			regPattern = "[0-9]{2}\\/[0-9]{2}\\/[0-9]{4}"
			matches = re.findall(regPattern, offerNode.get_text())

			if len(matches) > 1:
				pubDate = matches[0]
				expDate = matches[1]
				print(link, title, desc, pubDate, expDate, '\n')


educarriere = Educarriere()
educarriere.scrape_all_pages()