from application.services.image_placeholder import ImagePlaceholder
class TestImagePlaceholder:
	"""Test suite for ImagePlaceholder methods."""
	
	def test_get_cached_images(self):
		images = ImagePlaceholder().get_cached_images('Technology')
		print(images)
		
		assert isinstance(images, list)

	def test_get_image(self):
		image = ImagePlaceholder().get_image('Technology')
		print(image)
		
		assert '.jpg' in image
