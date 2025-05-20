from CardFraud.config.configuration import ConfigurationManager
from CardFraud.component.data_training import ModelTraining
from logger import logging
import sys
from exception import CustomException

STAGE_NAME = "Data Training  Stage"


class DataTrainigPipeline:

    def __init__(self):
        pass

    def main(self):

        try:
            data_config = ConfigurationManager()
            data_train_config = data_config.get_data_training_config()
            data_training = ModelTraining(data_train_config)
            data_training.run_training_pipeline()

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        logging.info(f">>>>>>>>>>Stage {STAGE_NAME} Started <<<<<<<<<<<")
        obj = DataTrainigPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>Stage {STAGE_NAME} Completed <<<<<<<<<<<")
    except Exception as e:
        raise CustomException(e, sys)
