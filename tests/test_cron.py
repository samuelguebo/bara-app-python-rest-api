from application.services.aej_cron import AEJCron
from application.services.atoo_cron import AtooCron
from application.services.educarriere_cron import EducarriereCron
from application.services.cron import Cron

class TestCron:
	"""
	Test suite for Cron objects
	and their relevant methods
	"""
	
	def test_extract_type(self):
		"""
		Test the extraction of type of job offer
		out of the job description
		"""
		url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
		content = Cron().extract_content(url, EducarriereCron.DETAILS_SELECTOR)
		type = Cron().extract_type(content.upper())
		print(type)
		
		assert 'CDI' in type

	def test_extract_content(self):
		"""
		Test the extracting full content of 
		out of URL provided
		"""
		url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
		selector = '.detailsOffre > div:not(.content-area)'
		content = Cron().extract_content(url, selector)
		
		assert len(content) > 100

	def test_extract_degrees(self):
		"""
		Test extraction of list of degrees
		from a job description
		"""
		url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
		cron = EducarriereCron()
		content = cron.extract_content(url, cron.DETAILS_SELECTOR)
		degrees = cron.extract_degrees(content.upper())
		print(degrees)
		
		assert len(degrees) == 4

	def test_extract_edu(self):
		"""
		Test the EducarriereCron class
		and its extraction operations
		"""
		url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
		cron = EducarriereCron()
		content = cron.extract_content(url, cron.DETAILS_SELECTOR)
		degrees = cron.extract_degrees(content.upper())
		type = cron.extract_type(content.upper())
		dates = cron.extract_dates(content)
		print('{} {} {}'.format(degrees, type, dates))
		
		assert len(degrees) == 4
	
	def test_extract_atoo(self):
		"""
		Test the AtooCron class
		and its extraction operations
		"""
		url = 'http://www.atoo.ci/emploi/jobs/conseiller-technique-pme-h-f/'
		cron = AtooCron()
		content = cron.extract_content(url, cron.DETAILS_SELECTOR)
		degrees = cron.extract_degrees(content.upper())
		type = cron.extract_type(content.upper())
		dates = cron.extract_dates(content)
		print('{} {} {}'.format(degrees, type, dates))
		
		assert len(degrees) == 4
	
	def test_extract_aej(self):
		"""
		Test the AEJCron class
		and its extraction operations
		"""
		url = 'https://www.agenceemploijeunes.ci/site/offres-emplois/14316'
		cron = AEJCron()
		content = cron.extract_content(url, cron.DETAILS_SELECTOR)
		degrees = cron.extract_degrees(content.upper())
		type = cron.extract_type(content.upper())
		dates = cron.extract_dates(content)
		print('{} {} {}'.format(degrees, type, dates))
		
		assert len(degrees) == 1
