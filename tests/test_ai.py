import pytest
import re
from config import Config
from application.services.cron import Cron
from application.dao.offer_dao import OfferDao
from application.models.offer import Offer
from application import db
from application.ai.classifier import Classifier
from application.services.educarriere_cron import EducarriereCron

class TestCron:
    """
    Test suite for the machine learning Classifier,
    triggering and evaluating AI predictions.
    """
    def test_predict(self):
        
        url = 'https://emploi.educarriere.ci/offre-69540-stagiaires-commerciaux.html'
        content = Cron().extractContent(url, EducarriereCron.DETAILS_SELECTOR)
        tags = Classifier().predict_category(Offer(url, "Test 1", content, "", ""))
        print(tags)
        
        assert True
        