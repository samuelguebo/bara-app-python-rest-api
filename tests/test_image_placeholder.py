from application.services.image_placeholder import ImagePlaceholder
from application.models.tag import Tag
from flask import Flask

class TestImagePlaceholder:
	"""
	Test suite for the ImagePlaceholder
	class and its relevant methods.
	"""
	
	app = Flask(__name__)

	def test_get_cached_images(self):
		"""
		Test how to fetch a list
		of cached images
		"""
		with self.app.test_request_context():
			images = ImagePlaceholder().get_cached_images('Informatique')
			print(images)
			
		assert isinstance(images, list)

	def test_get_image(self):
		"""
		Test how to generate a single
		random image
		"""
		
		with self.app.test_request_context():
			image = ImagePlaceholder().get_image([Tag('Informatique')])
			print(image)
		
		assert '.jpg' in image
