from dataclasses import dataclass

@dataclass
class DataValidationConfig:
    root_dir: str
    status_file: str
    schema_file: str
    data_file: str
