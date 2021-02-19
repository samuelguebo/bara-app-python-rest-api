from config import db, Config

class Degree(db.Model):     
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Degree {}>'.format(self.title)
