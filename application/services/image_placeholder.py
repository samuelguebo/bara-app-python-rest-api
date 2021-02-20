import os
from config import Config
from flask import request
import random

class ImagePlaceholder():
	"""
	Generates and manages a series of images
	that are cached in the static repository
	"""

	def __init__(self):
		self = self
	

	def get_image(self, tags):
		"""
		Provide randomly an image based on a given
		keyword related to the image

		:param keyword: a word related to the image
		"""
		if len(tags) > 0:
			images = self.get_cached_images(tags[0].title)
			
			if len(images) > 1:
				return images[random.randint(0, len(images)-1)]

		return False

	def get_cached_images(self, keyword):
		"""
		Browser through static folder (cache)
		and return a list of images
		"""
		images = []
		path  = Config.ROOT_FOLDER + '/static/images/' + keyword.lower()
		root_url = request.url_root + 'static/images/' + keyword.lower()
		if not os.path.exists(path):
			return images
		
		images = ['{}/{}'.format(root_url,  f) for f in os.listdir(path)]
		return images

