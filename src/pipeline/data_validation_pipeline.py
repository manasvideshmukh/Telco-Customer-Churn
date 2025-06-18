from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation
import logging

def start_data_validation():
    config = ConfigurationManager().get_data_validation_config()
    validator = DataValidation(config)

    logging.info(">>>>> Data Validation Started <<<<<")
    validator.validate()
    logging.info(">>>>> Data Validation Completed <<<<<")
