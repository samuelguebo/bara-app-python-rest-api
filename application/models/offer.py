from .. import db

class Offer(db.Model):   

    url = db.Column(db.String(64), primary_key=True, unique=True)
    title = db.Column(db.String(64))
    content = db.Column(db.String(64))
    pubDate = db.Column(db.String(64))
    expDate = db.Column(db.String(64))
    
    def __init__(self, url, title, content, pubDate, expDate):
        self.url = url
        self.title = title
        self.content = content
        self.pubDate = pubDate
        self.expDate = expDate

    def __repr__(self):
        return '<Offer {}>'.format(self.title)