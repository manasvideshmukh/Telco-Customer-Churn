from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    root_dir: str
    train_data_path: str
    test_data_path: str
    transformed_train_path: str
    transformed_test_path: str
    transformer_object_path: str
