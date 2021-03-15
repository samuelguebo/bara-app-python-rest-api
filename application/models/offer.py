from config import db, Config, SessionLocal, Base
from .degree import Degree
from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import DateTime
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from application.services.image_placeholder import ImagePlaceholder


class Offer(Base):
    __tablename__ = 'offer'
    url = Column(String(300), primary_key=True, unique=True)
    title = Column(String(300))
    type = Column(String(64), nullable=True, default='PENDING')
    status = Column(String(64), nullable=True)
    content = Column(Text())
    pub_date = Column(DateTime())
    exp_date = Column(DateTime())
    image = Column(String(300), nullable=True)

    def __init__(self, url, title, content, pub_date, exp_date):
        self.url = url
        self.title = title
        self.content = content
        self.pub_date = pub_date
        self.exp_date = exp_date

    def __repr__(self):
        return '<Offer {} {} {} {}>'.format(self.title, self.type,
                                            self.degrees, self.tags)

    def set_satus(self, status):
        self.status = status

    def set_type(self, type):
        self.type = type

    def set_image(self, tags):
        self.image = ImagePlaceholder().get_image(tags)

    # Many to Many relationship with Tag
    offer_tags_table = Table('offer_tags',
                             Base.metadata,
                             Column('tag_id', Integer, ForeignKey(
                                 'tag.id'), primary_key=True),
                             Column('offer_id', String(300), ForeignKey(
                                 'offer.url'), primary_key=True)
                             )
    tags = relationship('Tag', secondary=offer_tags_table, lazy='subquery',
                        backref=backref('offers', lazy=True))

    # Many to Many relationship with Degree
    offer_degrees_table = Table('offer_degrees',
                                Base.metadata,
                                Column('degree_id', Integer, ForeignKey(
                                    'degree.id'), primary_key=True),
                                Column('offer_id', String(300), ForeignKey(
                                    'offer.url'), primary_key=True)
                                )
    degrees = relationship('Degree', secondary=offer_degrees_table, lazy='subquery',
                           backref=backref('offers', lazy=True))

# Serialization


class DeegreeSchema(SQLAlchemySchema):
    class Meta:
        model = Degree
        load_instance = True

    title = auto_field()


class TagsSchema(SQLAlchemySchema):
    class Meta:
        model = Degree
        load_instance = True

    title = auto_field()


class OfferSchema(SQLAlchemySchema):
    class Meta:
        model = Offer
        include_relationships = True
        load_instance = True

    url = auto_field()
    title = auto_field()
    image = auto_field()
    pub_date = auto_field()
    exp_date = auto_field()
    type = auto_field()
    content = auto_field()
    degrees = fields.Nested(DeegreeSchema, many=True)
    tags = fields.Nested(TagsSchema, many=True)
