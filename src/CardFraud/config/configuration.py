from CardFraud.utils.common import read_yaml, create_directories
from CardFraud.constant import *
from CardFraud.entity.config_entity import DataIngestionConfig, DataPreprocessingConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        data_ingestion_config = DataIngestionConfig(
            data_source=self.config.data_ingestion.data_source,
            processed_data_dir=self.config.data_ingestion.processed_data_dir,
            train_file=self.config.data_ingestion.train_file,
            test_file=self.config.data_ingestion.test_file
        )

        return data_ingestion_config

    def get_data_Prepropcssing_config(self) -> DataPreprocessingConfig:
        data_preprocessing_config = DataPreprocessingConfig(
            train_file_path=self.config.data_preprocessing.train_file_path,
            test_file_path=self.config.data_preprocessing.test_file_path,
            processed_data_dir=self.config.data_preprocessing.processed_data_dir,
            processed_train_file=self.config.data_preprocessing.processed_train_file,
            processed_test_file=self.config.data_preprocessing.processed_test_file,
            remove_duplicates=self.params.preprocessing.remove_duplicates,
            scaler_type=self.params.preprocessing.scaler_type,
            sampling_method=self.params.preprocessing.sampling_method)

        return data_preprocessing_config
