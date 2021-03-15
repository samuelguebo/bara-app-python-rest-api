from application.models.tag import Tag
from application.models.degree import Degree
from application.models.offer import Offer
from config import SessionLocal, engine, Base


class OfferDao():

    def __init__(self):
        self = self
        self.db = SessionLocal()

        # In case table does not exist
        Base.metadata.create_all(bind=engine)

    def create(self, offer):
        try:
            self.db.add(offer)
            self.db.commit()
            return self.fetch(1).first()

        except Exception as e:
            print(e.args)
            return e.args

    def fetch(self, n):
        return self.db.query(Offer).limit(n)

    def get_tags(self):
        return self.db.query(Tag).all()

    def find_by_tag(self, title):
        return self.db.query(Offer).join(Offer.tags).filter(Tag.title == title).all()

    def find_tag_by_title(self, title):
        return self.db.query(Tag).filter(Tag.title == title).first()

    def find_degree_by_title(self, title):
        return self.db.query(Degree).filter(Degree.title == title).first()
