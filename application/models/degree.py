from config import db, Config, SessionLocal, Base
from sqlalchemy import Column, Integer, String, Text


class Degree(Base):   
	__tablename__ = 'degree'

	id = Column(Integer, primary_key=True)
	title = Column(String(64))

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return '<Degree {}>'.format(self.title)
