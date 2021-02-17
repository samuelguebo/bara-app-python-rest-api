from application.services.aej_cron import AEJCron
from application.models.degree import Degree
from application.services.atoo_cron import AtooCron
import pytest
import re
from config import Config
from application.services.cron import Cron
from application.services.educarriere_cron import EducarriereCron
from application.dao.offer_dao import OfferDao
from application.models.offer import Offer
from application import db

class TestCron:
	"""Test for cron operations."""
	'''
	def test_extract_type(self):
		url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
		content = Cron().extractContent(url, EducarriereCron.DETAILS_SELECTOR)
		type = Cron().extractType(content.upper())
		print(type)
		assert 'CDI' in type

	def test_extract_content(self):
		url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
		selector = '.detailsOffre > div:not(.content-area)'
		content = Cron().extractContent(url, selector)
		assert len(content) > 100

	def test_extract_degrees_edu(self):
		url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
		content = Cron().extractContent(url, EducarriereCron.DETAILS_SELECTOR)
		degrees = Cron().extractDegrees(content.upper())
		print(degrees)
		assert len(degrees) == 4
	def test_extract_degrees_atoo(self):
		url = 'http://www.atoo.ci/emploi/jobs/conseiller-technique-pme-h-f/'
		content = Cron().extractContent(url, AtooCron.DETAILS_SELECTOR)
		degrees = Cron().extractDegrees(content.upper())
		print(degrees)
		assert len(degrees) == 4
	'''

	
	def test_extract_aej(self):
		url = 'https://www.agenceemploijeunes.ci/site/offres-emplois/14316'
		cron = AEJCron()
		content = cron.extractContent(url, cron.DETAILS_SELECTOR)
		degrees = cron.extractDegrees(content.upper())
		type = cron.extractType(content.upper())
		dates = cron.extract_dates(content)
		print('{} {} {}'.format(degrees, type, dates))
		assert len(degrees) == 1
		
	