from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    data_source: Path
    processed_data_dir: Path
    train_file: Path
    test_file: Path
