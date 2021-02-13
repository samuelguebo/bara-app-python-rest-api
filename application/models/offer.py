from .. import db

class Offer(db.Model):   

    url = db.Column(db.VARCHAR(300), primary_key=True, unique=True)
    title = db.Column(db.VARCHAR(300))
    content = db.Column(db.VARCHAR(300))
    pubDate = db.Column(db.VARCHAR(300))
    expDate = db.Column(db.VARCHAR(300))
    
    def __init__(self, url, title, content, pubDate, expDate):
        self.url = url
        self.title = title
        self.content = content
        self.pubDate = pubDate
        self.expDate = expDate

    def __repr__(self):
        return '<Offer {}>'.format(self.title)