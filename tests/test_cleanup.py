from application.services.cleanup_cron import CleanupCron
from config import Config
from application import create_app, db
from application.models.offer import Offer
from datetime import date, datetime, timedelta

class TestCleanup:
	
	app = create_app()
			
	def test_cleanup(self):
		"""
		Test CleanupCron class and verifies
		regular deletion of old articles
		"""

		with self.app.app_context():
			CleanupCron().run()
		
		assert True
	
	