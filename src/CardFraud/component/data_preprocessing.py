import pandas as pd
from exception import CustomException
from logger import logging
import sys
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from imblearn.over_sampling import SMOTE
from pathlib import Path
from CardFraud.config.configuration import DataPreprocessingConfig
import os



class Preprocessing:
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config

    def load_data(self) -> pd.DataFrame:
        try:
            data_train = pd.read_csv(self.config.train_file_path)
            data_test = pd.read_csv(self.config.test_file_path)
            logging.info(
                f"Train Data loaded successfully. Shape: {data_train.shape}")
            logging.info(
                f"Test Data loaded successfully. Shape: {data_test.shape}")

        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise
        return data_train, data_test

    def remove_duplicate(self, data: pd.DataFrame):
        if self.config.remove_duplicates:
            initial_shape = data.shape
            unique_data = data.drop_duplicates()
            logging.info(
                f"Removed duplicates. Shape before: {initial_shape}, after: {data.shape}")
        return unique_data

    def apply_oversampling(self, train_data: pd.DataFrame) -> pd.DataFrame:
        try:
            logging.info("Applying SMOTE for oversampling...")

            X_train = train_data.drop("Class", axis=1)
            y_train = train_data["Class"]
            smote = SMOTE(sampling_strategy="auto", random_state=42)
            X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
            # Recreate DataFrame
            oversampled_data = pd.DataFrame(
                X_resampled, columns=X_train.columns)
            oversampled_data["Class"] = y_resampled

            logging.info(f"Data after oversampling: {oversampled_data.shape}")
            return oversampled_data
        except Exception as e:
            logging.error(f"Error during oversampling: {e}")
            raise CustomException(e, sys)

    def _initialize_scaler(self):
        """
        Initialize the scaler based on the configuration.

        Returns:
            Scaler object (StandardScaler or MinMaxScaler).
        """
        scaler_type = self.config.scaler_type

        if scaler_type == "StandardScaler":
            return StandardScaler()
        elif scaler_type == "MinMaxScaler":
            return MinMaxScaler()
        else:
            raise ValueError(f"Unsupported scaler type: {scaler_type}")

    def data_scaling(self, train: pd.DataFrame, test: pd.DataFrame):
        try:
            self.scaler = self._initialize_scaler()

            X_train = train.drop("Class", axis=1)
            y_train = train["Class"]

            X_test = test.drop("Class", axis=1)
            y_test = test["Class"]

            X_train_scaled = self.scaler.fit_transform(X_train)
            X_test_scaled = self.scaler.transform(X_test)

            X_train_scaled = pd.DataFrame(
                X_train_scaled, columns=X_train.columns)
            X_train_scaled["Class"] = y_train.values

            X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)
            X_test_scaled["Class"] = y_test.values
            logging.info(f"Data  Scaled sucessfully")

            return X_train_scaled, X_test_scaled

        except Exception as e:
            logging.error(f"Error during scaling: {e}")
            raise CustomException(e, sys)

    def data_save(self, data: pd.DataFrame, filepath: Path):
        os.makedirs(self.config.processed_data_dir, exist_ok=True)
        data.to_csv(os.path.join(
            self.config.processed_data_dir, filepath), index=False)
        logging.info("data Saved succssfully")

    def preprocessing(self):
        try:
            logging.info("Starting preprocessing pipeline...")
            data_train, data_test = self.load_data()

            logging.info("Removing duplicates...")
            data_train = self.remove_duplicate(data_train)
            data_test = self.remove_duplicate(data_test)

            logging.info("Applying oversampling on training data...")
            data_train = self.apply_oversampling(data_train)

            logging.info("Scaling data...")
            X_train_scaled, X_test_scaled = self.data_scaling(
                data_train, data_test)

            logging.info("Saving preprocessed data...")
            self.data_save(X_train_scaled, Path(
                self.config.processed_train_file))
            self.data_save(X_test_scaled, Path(
                self.config.processed_test_file))

            logging.info("Preprocessing pipeline completed successfully.")

        except Exception as e:
            logging.error(f"Error in preprocessing pipeline: {e}")
            raise CustomException(e, sys)
