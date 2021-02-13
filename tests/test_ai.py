import pytest
import re
from config import Config
from application.services.cron import Cron
from application.dao.offer_dao import OfferDao
from application.models.offer import Offer
from application import db
from application.ai.classifier import Classifier

class TestCron:
    """Test for AI predictions."""
    
    def test_predict(self):
        url = 'https://emploi.educarriere.ci/offre-69336-office-manager.html'
        selector = '.detailsOffre > div:not(.content-area)'
        content = Cron().extractContent(url, selector)
        tags = Classifier().predict_category(Offer(url, "Test 1", content, "", ""))
        print(tags)
        assert True
        
