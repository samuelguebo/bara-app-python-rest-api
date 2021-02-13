import pytest
import re
from config import Config
from application.services.cron import Cron
from application.dao.offer_dao import OfferDao
from application.models.offer import Offer
from application import db

class TestCron:
    """Test for cron operations."""
    
    def test_extract_degrees(self):

        url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
        selector = '.detailsOffre > div:not(.content-area)'
        content = Cron().extractContent(url, selector)
        degrees = Cron().extractWithRegex(content.upper(), Config.DEGREE_REGEX)
        degrees = list(set(degrees))
        print(degrees)
        assert 'BAC+3' in degrees

    def test_extract_type(self):
        url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
        selector = '.detailsOffre > div:not(.content-area)'
        content = Cron().extractContent(url, selector)
        type = Cron().extractType(content.upper())
        print(type)
        assert 'CDI' in type

    def test_extract_content(self):
        url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
        selector = '.detailsOffre > div:not(.content-area)'
        content = Cron().extractContent(url, selector)
        assert len(content) > 100

        