from src.CardFraud.pipeline.stage_01_dataingestion import DataIngestionPipeline
from src.logger import logging
from src.exception import CustomException
import sys


STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logging.info(f">>>>>>>>>>Stage {STAGE_NAME} Started <<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>Stage {STAGE_NAME} Completed <<<<<<<<<<<")
    except Exception as e:
        raise CustomException(e, sys)
