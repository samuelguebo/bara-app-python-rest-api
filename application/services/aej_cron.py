from .cron import Cron

class AEJCron(Cron):
	ID = "AEJ"
	ROOT_URL = "https://www.agenceemploijeunes.ci/site/"
	URL_LIST = ROOT_URL + "offres-emplois"
	CACHE_DELAY = 6 # six hours
	OFFERS_SELECTOR = '.aej_offr'
	TITLES_SELECTOR = 'aej_joblib a'
	DESC_SELECTOR = '.job-type'	
	DETAILS_SELECTOR = '#DIV_2 .col-md-8'

	def run(self):
		for i in range(1):
			url = '{}?page={}'.format(self.URL_LIST, i)
			self.scrape_home_page(url)