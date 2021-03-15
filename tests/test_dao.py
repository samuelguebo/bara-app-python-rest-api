from flask import Flask, jsonify
from application.dao.offer_dao import OfferDao
from application.ai.classifier import Classifier
from application.models.tag import Tag
from application.models.offer import Offer, OfferSchema
from application.services.educarriere_cron import EducarriereCron
from config import db
from application import create_app


class TestDAO:
    """
    Test suite for Database operations.
    It covers insertion and other frequent
    tasks that involve database interaction
    """

    app = create_app()

    def setUp(self):
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()

    def test_insert(self):
        with self.app.app_context():
            title = 'Community manager senior'
            url = 'https://emploi.educarriere.ci/offre-68967-community-manager-senior.html'
            cron = EducarriereCron(page_number=1)
            content = cron.extract_content(url, cron.DETAILS_SELECTOR)
            dates = cron.extract_dates(content)
            pub_date, exp_date = (dates[0], dates[1])
            offer = Offer(url, title, content, pub_date, exp_date)
            offer.degrees = cron.extract_degrees(offer.content)
            offer.set_type(cron.extract_type(offer.content))
            offer.set_satus(cron.PENDING)

            # avoid recreating tag
            dao = OfferDao()
            generated_tags = Classifier().predict_category(offer)
            for i in range(len(generated_tags)):
                if len(dao.find_tag_by_title(generated_tags[i])) > 0:
                    generated_tags[i] = dao.find_tag_by_title(
                        generated_tags[i])
                else:
                    generated_tags[i] = Tag(generated_tags[i])

            offer.tags = generated_tags

            # Save to database
            result = dao.create(offer)
            print(offer)
            print(type(result))

        assert type(result) in [Offer, tuple]

    def test_find_tag_by_title(self):
        tags = OfferDao().find_tag_by_title('Finance')

        assert type(tags) is list
