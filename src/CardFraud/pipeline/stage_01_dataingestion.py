from CardFraud.config.configuration import ConfigurationManager
from CardFraud.component.data_ingestion import DataIngestion
from exception import CustomException
from logger import logging
import sys

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion()


# if __name__ == "__main__":
#     try:
#         logging.info(f">>>>>>>>>>Stage {STAGE_NAME} Started <<<<<<<<<<<")
#         obj = DataIngestionPipeline()
#         obj.main()
#         logging.info(f">>>>>>>>>>Stage {STAGE_NAME} Completed <<<<<<<<<<<")
#     except Exception as e:
#         raise CustomException(e, sys)
