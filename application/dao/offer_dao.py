class OfferDao():   
    
    def __init__(self, db):
        self = self
        self.db = db

        # In case table does not exist
        db.create_all()

    def create(self, offer):
        self.db.session.merge(offer)
        self.db.session.commit()