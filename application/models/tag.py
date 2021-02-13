from .. import db

class Tag(db.Model): 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(300))

    def __init__(self, title):
        self.title = title

        