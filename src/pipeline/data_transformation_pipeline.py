from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
import logging

STAGE_NAME = "Data Transformation Stage"

def start_data_transformation():
    try:
        logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.initiate_data_transformation()
        
        logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\n")
    
    except Exception as e:
        logging.exception(e)
        raise e
