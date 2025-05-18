from CardFraud.entity.config_entity import DataIngestionConfig
from CardFraud.config.configuration import ConfigurationManager
from sklearn.model_selection import train_test_split
import pandas as pd
from exception import CustomException
from logger import logging
import sys
import os
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def read_data(self) -> pd.DataFrame:

        try:
            data = pd.read_csv(self.config.data_source)
            logging.info("data Read succssfully")
            return data
        except Exception as e:
            raise CustomException(e, sys)

    def save_data(self, data: pd.DataFrame, filepath: Path):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        data.to_csv(filepath, index=False)
        logging.info("data Saved succssfully")

    def split_data(self, data: pd.DataFrame):
        try:

            train_data, test_data = train_test_split(
                data, test_size=0.2, random_state=42)

            self.save_data(train_data, os.path.join(
                self.config.processed_data_dir, self.config.train_file))
            self.save_data(test_data, os.path.join(
                self.config.processed_data_dir, self.config.test_file))
            logging.info("data Split succssfully")
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> None:

        data = self.read_data()
        self.split_data(data)
