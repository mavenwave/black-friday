import os
import pickle

import numpy as np



class MyPredictor(object):
    """An example Predictor for an AI Platform custom prediction routine."""

    def __init__(self, model): #, preprocessor
        """Stores artifacts for prediction. Only initialized via `from_path`.
        """
        self._model = model
        #self._preprocessor = preprocessor

    def predict(self, instances, **kwargs):
        """Performs custom prediction.

        Preprocesses inputs, then performs prediction using the trained Keras
        model.

        Args:
            instances: A list of prediction input instances.
            **kwargs: A dictionary of keyword args provided as additional
                fields on the predict request body.

        Returns:
            A list of outputs containing the prediction results.
        """

        outputs = self._model.predict(instances)
        pred = outputs.tolist()[0]
        product_1_cat = pred.index(max(pred)) + 1
        return 'Product Category {}'.format(str(product_1_cat))



    @classmethod
    def from_path(cls, model_dir):
        """Creates an instance of MyPredictor using the given path.

        This loads artifacts that have been copied from your model directory in
        Cloud Storage. MyPredictor uses them during prediction.

        Args:
            model_dir: The local directory that contains the trained Keras
                model and the pickled preprocessor instance. These are copied
                from the Cloud Storage model directory you provide when you
                deploy a version resource.

        Returns:
            An instance of `MyPredictor`.
        """
        model_path = os.path.join(model_dir, 'model.pkl')
        model = pickle.load(open(model_path,'rb'))

        """
        preprocessor_path = os.path.join(model_dir, 'preprocessor.pkl')
        with open(preprocessor_path, 'rb') as f:
            preprocessor = pickle.load(f)
        """

        return cls(model) #, preprocessor