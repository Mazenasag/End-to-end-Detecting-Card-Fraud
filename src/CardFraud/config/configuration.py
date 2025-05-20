from CardFraud.utils.common import read_yaml, create_directories
from CardFraud.constant import *
from CardFraud.entity.config_entity import DataIngestionConfig, DataPreprocessingConfig, DataTrainingConfig


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
            artifacts_data_dir=self.config.artifactes.artifactes_dir,
            train_file_path=self.config.data_preprocessing.train_file_path,
            test_file_path=self.config.data_preprocessing.test_file_path,
            processed_data_dir=self.config.data_preprocessing.processed_data_dir,
            processed_train_file=self.config.data_preprocessing.processed_train_file,
            processed_test_file=self.config.data_preprocessing.processed_test_file,
            remove_duplicates=self.params.preprocessing.remove_duplicates,
            scaler_type=self.params.preprocessing.scaler_type,
            sampling_method=self.params.preprocessing.sampling_method)

        return data_preprocessing_config

    def get_data_training_config(self) -> DataTrainingConfig:
        data_training_config = DataTrainingConfig(
            processed_train_path=self.config.data_training.processed_train_path,
            processed_test_path=self.config.data_training.processed_test_path,
            artifacts_data_dir=self.config.artifactes.artifactes_dir,
            model_pkl_file=self.config.data_training.model_pkl_file,
            max_depth=self.params.training_params.max_depth,
            min_samples_split=self.params.training_params.min_samples_split,
            min_samples_leaf=self.params.training_params.min_samples_leaf,
            max_features=self.params.training_params.max_features,
            n_estimators=self.params.training_params.n_estimators,
            learning_rate=self.params.training_params.learning_rate
        )
        return data_training_config
