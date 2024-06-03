import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model
from dataclasses import dataclass
import sys
import os

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,  train_features_array,train_target_array,test_features_array,test_target_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_features_array,
                train_target_array,
                test_features_array,
                test_target_array
            )

            logistic_regression = LogisticRegression()

            model_report = evaluate_model(X_train, y_train, X_test, y_test, {'LogisticRegression': logistic_regression})
            logging.info(f'Model Report: {model_report}')

            best_model_name = 'LogisticRegression'
            best_model_score = model_report[best_model_name]

            logging.info(f'Best Model Found, Model Name: {best_model_name}, Score: {best_model_score}')

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=logistic_regression
            )
          
        except Exception as e:
            logging.info('Exception occurred at Model Training')
            raise CustomException(e, sys)
