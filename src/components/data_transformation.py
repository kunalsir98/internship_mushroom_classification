import os
import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            # Define categorical columns
            cat_features = ['bruises', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-root', 'ring-type', 'spore-print-color']

            # Define categorical pipeline
            cat_pipeline = Pipeline(steps=[
                ("one_hot", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
            ])

            # Creating preprocessor object
            preprocessor = ColumnTransformer([
                ("cat_pipeline", cat_pipeline, cat_features)
            ])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("reading train and test data")
            
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("obtaining preprocessor object")
            
            preprocessor_obj = self.get_data_transformer_object()
            
            target_column_name = "class"
            
            input_feature_train_df = train_df.drop([target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop([target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info("applying preprocessor object to train and test input features")
            
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
            
            logging.info("applying label encoder to target data")
            
            le = LabelEncoder()
            
            target_train_arr = le.fit_transform(target_feature_train_df)
            target_test_arr = le.transform(target_feature_test_df)
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            
            return ( 
                input_feature_train_arr,
                target_train_arr,
                input_feature_test_arr,
                target_test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
                       
        except Exception as e:
            raise CustomException(e,sys)