from pickle5 import pickle
import requests

class Classifier:
	"""
	Text classification using pre-trained model
	previsouly serialized using Pickle
	"""

	def predict_category(self, offer):
		"""
		Classify job offer and generate
		relevant tags or categories

		:param offer: Offer object 
		"""
		
		# load saved model and vectorizer
		model_path = '.job_classification_model.pickle'
		vect_path = '.job_classification_vect.pickle'

		saved_model = pickle.load(open(model_path, 'rb'))
		saved_vect = pickle.load(open(vect_path, 'rb'))

		# Custom categories based on specific domain knowledge 
		tags = {
			0: 'Comptabilité / Finance',
			1: 'Gestion de projets',
			2: 'Communication / Marketing',
			3: 'Entrepeneuriat',
			4: 'Informatique',
			5: 'Management',
			6: 'Logistique / Transport',
			7: 'Communication / Marketing',
		}
		
		tag_values = saved_model.transform(saved_vect.transform([offer.desc]))

		# do the prediction
		dominant_tag_id = tag_values.argmax(axis=1)[0]
		predicted_tag = tags[dominant_tag_id]

		return predicted_tag