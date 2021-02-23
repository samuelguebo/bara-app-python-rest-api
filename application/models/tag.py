from config import Config, db, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
from sqlalchemy import Table

class Tag(Base): 
	__tablename__ = 'tag'

	id = Column(Integer, primary_key=True)
	title = Column(String(300))

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return '<Tag {}>'.format(self.title)