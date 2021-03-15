from pickle5 import pickle
import inspect
import requests


class Classifier:
    """
    Text classification using pre-trained model
    previsouly serialized using Pickle
    """

    def __init__(self):
        pass

    def predict_category(self, offer):
        """
        Classify job offer and generate
        relevant tags or categories

        :param offer: Offer object 
        """

        # load saved model and vectorizer
        model_path = 'application/ai/job_classification_model.pickle'
        vect_path = 'application/ai/job_classification_vect.pickle'

        saved_model = pickle.load(open(model_path, 'rb'))
        saved_vect = pickle.load(open(vect_path, 'rb'))

        # Custom categories based on specific domain knowledge
        tags = {
            0: 'Marketing',
            1: 'Finance',
            2: 'Informatique',
            3: 'Assistanat',
            4: 'Transport',
            5: 'Marketing',
            6: 'Management',
            7: 'Communication',
            8: 'Technicien',
            9: 'Entrepreneuriat'
        }

        tag_values = saved_model.transform(
            saved_vect.transform([offer.content]))

        # do the prediction
        dominant_tag_ids = tag_values.argmax(axis=1)
        predicted_tags = [tags[x] for x in dominant_tag_ids]

        return predicted_tags
