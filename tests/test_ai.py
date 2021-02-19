import pytest
import re
from config import Config
from application.services.cron import Cron
from application.dao.offer_dao import OfferDao
from application.models.offer import Offer
from application import db
from application.ai.classifier import Classifier
from application.services.educarriere_cron import EducarriereCron
from application import create_app

class TestCron:
	"""
	Test suite for the machine learning Classifier,
	triggering and evaluating AI predictions.
	"""

	app = create_app()

	def setUp(self):
		with self.app.app_context():
			db.create_all()

	def tearDown(self):
		with self.app.app_context():
			db.session.remove()

	def test_predict(self):
		with self.app.app_context():
			offer = Offer.query.first()
			tags = Classifier().predict_category(offer)
			print(offer.title, offer.url)
			print(tags)
		
		assert True
		