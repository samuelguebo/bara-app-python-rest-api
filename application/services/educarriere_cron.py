from .cron import Cron

class EducarriereCron(Cron):
	ID = "EDUCARRIERE"
	ROOT_URL = "https://emploi.educarriere.ci/"
	URL_LIST = ROOT_URL + "nos-offres"
	CACHE_DELAY = 6 # six hours
	OFFERS_SELECTOR = 'ul#myList .box.row'
	TITLES_SELECTOR = '.text-col h4 a'
	DESC_SELECTOR = '.text-col .entry-title a'	
	DETAILS_SELECTOR = '.detailsOffre > div:not(.content-area)'

	def run(self):
		for i in range(self.page_number):
			url = '{}?page1={}'.format(self.URL_LIST, i)
			self.scrape_home_page(url)