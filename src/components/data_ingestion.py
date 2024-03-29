import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_cleaning import DataCleaning, DataCleaningConfig
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook/data/FS_data.csv")
            logging.info('Read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

    

            logging.info("Ingestion of the data is completed")

            return self.ingestion_config.raw_data_path
            return self.ingestion_config.train_data_path
            return self.ingestion_config.test_data_path


            
        except Exception as e:
            raise CustomException(e,sys)


        
if __name__=="__main__":
    obj=DataIngestion()
    raw_data_imgestion=obj.initiate_data_ingestion()

    obj2=DataCleaning()
    raw_arr=obj2.initiate_data_cleaning() 

    obj3 = DataTransformation()
    train_arr, test_arr, obj_file_path = obj3.initiate_data_transformation()

    obj4 = ModelTrainer()
    print(obj4.initiate_model_trainer(train_arr,test_arr))








 