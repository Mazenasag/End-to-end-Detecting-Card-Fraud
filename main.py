from src.CardFraud.pipeline.stage_01_dataingestion import DataIngestionPipeline
from src.CardFraud.pipeline.stage_02_datapreprocessing import DataPreprocessingPipeline
from src.logger import logging
from src.exception import CustomException
import sys


STAGE_NAME_1 = "Data Ingestion Stage"
STAGE_NAME_2 = "Data Preprocessing"

if __name__ == "__main__":
    try:
        logging.info(f"Starting {STAGE_NAME_1}")
        data_ingestion = DataIngestionPipeline()
        data_ingestion.main()
        logging.info(f"Completed {STAGE_NAME_1}")

        logging.info(f"Starting {STAGE_NAME_2}")
        data_preprocessing = DataPreprocessingPipeline()
        data_preprocessing.main()
        logging.info(f"Completed {STAGE_NAME_2}")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise CustomException(e, sys)
