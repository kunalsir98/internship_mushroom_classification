import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred

        except Exception as e:
            logging.info("Exception occurred in prediction")
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, bruises, gill_spacing, gill_size, gill_color, stalk_root, ring_type, spore_print_color, class_label):
        self.bruises = bruises
        self.gill_spacing = gill_spacing
        self.gill_size = gill_size
        self.gill_color = gill_color
        self.stalk_root = stalk_root
        self.ring_type = ring_type
        self.spore_print_color = spore_print_color
        
        

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'bruises': [self.bruises],
                'gill-spacing': [self.gill_spacing],
                'gill-size': [self.gill_size],
                'gill-color': [self.gill_color],
                'stalk-root': [self.stalk_root],
                'ring-type': [self.ring_type],
                'spore-print-color': [self.spore_print_color],
                 
                
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occurred in prediction pipeline')
            raise CustomException(e, sys)
