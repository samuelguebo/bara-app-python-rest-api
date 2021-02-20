from application.models.offer import Offer
from config import Config, db
from datetime import datetime, timedelta
from application.services.cron import Cron


class CleanupCron(Cron):
	ID = "CLEANUP"
	CACHE_DELAY = 12 # six hours
	
	def run(self):
		"""
		Deletion expired articles
		on a regular basis
		"""
		cleanup_deadline = (datetime.now() -  timedelta(
			days=int(Config.CLEANUP_DEADLINE)))
		expired_offers = Offer.query.filter(
			Offer.pub_date <= cleanup_deadline).all()

		for expired_offer in expired_offers:
			db.session.delete(expired_offer)
		db.session.commit()
		
		return True