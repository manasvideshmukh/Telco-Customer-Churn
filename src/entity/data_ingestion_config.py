from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_file: str
    raw_data: str
    train_data: str
    test_data: str
    test_size: float
    random_state: int
