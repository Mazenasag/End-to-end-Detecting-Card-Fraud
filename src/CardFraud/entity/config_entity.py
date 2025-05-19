from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    data_source: Path
    processed_data_dir: Path
    train_file: Path
    test_file: Path


@dataclass(frozen=True)
class DataPreprocessingConfig:
    train_file_path: Path
    test_file_path: Path
    processed_data_dir: Path
    processed_train_file: Path
    processed_test_file: Path
    remove_duplicates: bool
    scaler_type: str
    sampling_method: str
