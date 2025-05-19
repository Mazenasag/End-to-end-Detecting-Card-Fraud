from CardFraud.config.configuration import ConfigurationManager
from CardFraud.component.data_preprocessing import Preprocessing
from exception import CustomException
from logger import logging
import sys

STAGE_NAME = "Data Ingestion Stage"


class DataPreprocessingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_processing_config = config.get_data_Prepropcssing_config()
        data_processing = Preprocessing(config=data_processing_config)
        data_processing.preprocessing()
