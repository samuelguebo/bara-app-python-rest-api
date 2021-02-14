from .. import db
from .tag import Tag
from .degree import Degree
from sqlalchemy_serializer import SerializerMixin

class Offer(db.Model, SerializerMixin):   

    url = db.Column(db.VARCHAR(300), primary_key=True, unique=True)
    title = db.Column(db.VARCHAR(300))
    type = db.Column(db.String(64), nullable=True, default='PENDING')
    status = db.Column(db.String(64), nullable=True)
    content = db.Column(db.Text())
    pubDate = db.Column(db.VARCHAR(300))
    expDate = db.Column(db.VARCHAR(300))
    
    # JSON Serialization
    serialize_only = ('url', 'title', 'type', 'pubDate', 'expDate')
    serialize_rules = ('-tags', '-degrees')

    def __init__(self, url, title, content, pubDate, expDate):
        self.url = url
        self.title = title
        self.content = content
        self.pubDate = pubDate
        self.expDate = expDate

    def __repr__(self):
        return '<Offer {} {}>'.format(self.title, self.type)

    def set_satus(self, status):
        self.status = status
    
    def set_type(self, type):
        self.type = type
    
    # Many to Many relationship with Tag
    tags = db.Table('offer_tags',
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
        db.Column('offer_id', db.VARCHAR(300), db.ForeignKey('offer.url'), primary_key=True)
    )
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('offers', lazy=True))

    # Many to Many relationship with Degree
    degrees = db.Table('offer_degrees',
        db.Column('degree_id', db.Integer, db.ForeignKey('degree.id'), primary_key=True),
        db.Column('offer_id', db.VARCHAR(300), db.ForeignKey('offer.url'), primary_key=True)
    )
    degrees = db.relationship('Degree', secondary=degrees, lazy='subquery',
        backref=db.backref('offers', lazy=True))
