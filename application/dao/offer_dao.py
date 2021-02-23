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
            self.db.merge(offer)
            self.db.commit()
            return self.fetch(1).first()
            
        except Exception as e:
            return e.args
    
    def fetch(self, n):
        return self.db.query(Offer).limit(n)