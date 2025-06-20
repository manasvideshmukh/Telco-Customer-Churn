from dataclasses import dataclass
from typing import Dict

@dataclass
class ModelTrainerConfig:
    root_dir: str
    transformed_train_path: str
    transformed_test_path: str
    model_path: str
    target_column: str
    train_data_path: str
    test_data_path: str
    logistic_regression: Dict
    random_forest: Dict
    xgboost: Dict
