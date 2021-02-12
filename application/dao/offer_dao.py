class OfferDao():   
    
    def __init__(self, db):
        self = self

    def create(self, offer):
        self.db.session.add(self.offer)
        self.db.session.commit()