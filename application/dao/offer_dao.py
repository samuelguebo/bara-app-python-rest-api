from ..models.tag import Tag
from ..models.degree import Degree
from ..models.offer import Offer
class OfferDao():   
    
    def __init__(self, db):
        self = self
        self.db = db

        # In case table does not exist
        db.create_all()

    def create(self, offer):
        self.db.session.merge(offer)
        self.db.session.commit()

    def fetch(self, n):
        return Offer.query.limit(n)