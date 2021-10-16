from application.models.tag import Tag
from application.models.degree import Degree
from application.models.offer import Offer
from config import SessionLocal, engine, Base
from application.ai.classifier import Classifier


class OfferDao():

    def __init__(self):
        self = self
        self.db = SessionLocal()

        # In case table does not exist
        Base.metadata.create_all(bind=engine)

    def create_or_update_offer(self, offer):
        try:
            cached_offer = self.find_by_url(offer.url)
            if type(cached_offer) is Offer:
                return cached_offer

            self.db.add(offer)
            self.db.commit()
            return self.db.fetch(1).first()

        except Exception as e:
            # print(e.args)
            self.db.rollback()
            return e.args

    def create_or_update_tags(self, offer):
        """
        Avoid recreating tags
        """
        generated_tags = Classifier().predict_category(offer)
        for i in range(len(generated_tags)):
            cached_tag = self.find_tag_by_title(generated_tags[i])
            if cached_tag is not None:
                generated_tags[i] = cached_tag
            else:
                generated_tags[i] = Tag(generated_tags[i])
        return generated_tags

    def create_or_update_degrees(self, offer, cron):
        """
        Avoid recreating degrees
        """
        generated_degrees = cron.extract_degrees(offer.content)
        for i in range(len(generated_degrees)):
            cached_degree = self.find_degree_by_title(
                generated_degrees[i].title)
            if cached_degree is not None:
                generated_degrees[i] = cached_degree
            else:
                generated_degrees[i] = Degree(generated_degrees[i])
        return generated_degrees

    def fetch(self, n):
        return self.db.query(Offer).limit(n)

    def get_tags(self):
        return self.db.query(Tag).all()

    def find_by_tag(self, title):
        return self.db.query(Offer).join(Offer.tags).filter(Tag.title == title).all()

    def find_by_url(self, url):
        return self.db.query(Offer).filter(Offer.url == url).first()

    def find_by_title(self, title):
        return self.db.query(Offer).filter(Offer.content.contains(title)).all()

    def find_tag_by_title(self, title):
        return self.db.query(Tag).filter(Tag.title == title).first()

    def find_degree_by_title(self, title):
        return self.db.query(Degree).filter(Degree.title == title).first()
