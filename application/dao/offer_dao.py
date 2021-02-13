from ..models.tag import Tag
from ..models.degree import Degree
class OfferDao():   
    
    def __init__(self, db):
        self = self
        self.db = db

        # In case table does not exist
        db.create_all()

    def create(self, offer):
        offer.tags.append(Tag("Technology"))
        offer.degrees.append(Degree("BAC+5"))
        offer.tags.append(Tag("Privacy"))
        offer.set_satus('PENDING')
        offer.set_type('CDI')
        self.db.session.merge(offer)
        self.db.session.commit()