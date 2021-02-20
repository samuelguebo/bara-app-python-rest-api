from config import Config, db
from .degree import Degree
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from application.services.image_placeholder import ImagePlaceholder

class Offer(db.Model):   	
	url = db.Column(db.VARCHAR(300), primary_key=True, unique=True)
	title = db.Column(db.VARCHAR(300))
	type = db.Column(db.String(64), nullable=True, default='PENDING')
	status = db.Column(db.String(64), nullable=True)
	content = db.Column(db.Text())
	pub_date = db.Column(db.DateTime())
	exp_date = db.Column(db.DateTime())
	image = db.Column(db.VARCHAR(300), nullable=True)

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
	offer_tags_table = db.Table('offer_tags',
		db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
		db.Column('offer_id', db.VARCHAR(300), db.ForeignKey('offer.url'), primary_key=True)
	)
	tags = db.relationship('Tag', secondary=offer_tags_table, lazy='subquery',
		backref=db.backref('offers', lazy=True))

	# Many to Many relationship with Degree
	offer_degrees_table = db.Table('offer_degrees',
		db.Column('degree_id', db.Integer, db.ForeignKey('degree.id'), primary_key=True),
		db.Column('offer_id', db.VARCHAR(300), db.ForeignKey('offer.url'), primary_key=True)
	)
	degrees = db.relationship('Degree', secondary=offer_degrees_table, lazy='subquery',
		backref=db.backref('offers', lazy=True))
	
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
