from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class DataIngestionConfig:
    data_source: Path
    processed_data_dir: Path
    train_file: Path
    test_file: Path


@dataclass(frozen=True)
class DataPreprocessingConfig:
    artifacts_data_dir: Path
    train_file_path: Path
    test_file_path: Path
    processed_data_dir: Path
    processed_train_file: Path
    processed_test_file: Path
    remove_duplicates: bool
    scaler_type: str
    sampling_method: str

@dataclass(frozen=True)
class DataTrainingConfig:
    processed_train_path: Path
    processed_test_path: Path
    artifacts_data_dir: Path
    model_pkl_file: Path
    max_depth: List
    min_samples_split: List
    min_samples_leaf: List
    max_features: List
    n_estimators: List
    learning_rate: List