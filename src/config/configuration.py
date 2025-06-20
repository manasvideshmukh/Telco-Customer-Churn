import yaml
from src.entity.data_ingestion_config import DataIngestionConfig
from src.entity.data_transformation_config import DataTransformationConfig
from src.entity.data_validation_config import DataValidationConfig
from src.entity.model_trainer_config import ModelTrainerConfig

class ConfigurationManager:
    def __init__(self, config_path="config/config.yaml"):
        self.config = self.read_yaml(config_path)

    @staticmethod
    def read_yaml(path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']
        return DataIngestionConfig(
            root_dir=config["root_dir"],
            source_file=config["source_file"],
            raw_data=config["raw_data"],
            train_data=config["train_data"],
            test_data=config["test_data"],
            test_size=config["test_size"],
            random_state=config["random_state"]
        )

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config['data_transformation']
        return DataTransformationConfig(
            root_dir=config['root_dir'],
            train_data_path=config['train_data_path'],
            test_data_path=config['test_data_path'],
            transformed_train_path=config['transformed_train_path'],
            transformed_test_path=config['transformed_test_path'],
            transformer_object_path=config['transformer_object_path']
        )
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config["data_validation"]
        return DataValidationConfig(
            root_dir=config["root_dir"],
            status_file=config["status_file"],
            schema_file=config["schema_file"],
            data_file=config["data_file"]
        )

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config["model_trainer"]
        return ModelTrainerConfig(
            root_dir=config["root_dir"],
            transformed_train_path=config["transformed_train_path"],
            transformed_test_path=config["transformed_test_path"],
            model_path=config["model_path"],
            target_column=config["target_column"],
            train_data_path=config["train_data_path"],   # ✅ Newly added
            test_data_path=config["test_data_path"],     # ✅ Newly added
            logistic_regression=config["logistic_regression"],
            random_forest=config["random_forest"],
            xgboost=config["xgboost"]
        )
