from .cron import Cron

class AtooCron(Cron):
	ID = "ATOO"
	ROOT_URL = "http://www.atoo.ci/"
	URL_LIST = ROOT_URL + "emploi/jobs"
	CACHE_DELAY = 6 # six hours
	DETAILS_SELECTOR = '.job-desc'
	OFFERS_SELECTOR = 'article.loadmore-item'
	TITLES_SELECTOR = '.loop-item-title a'
	DESC_SELECTOR = '.job-type'	

	def run(self):
		for i in range(1):
			url = '{}/page/{}'.format(self.URL_LIST, i)
			self.scrape_home_page(url)