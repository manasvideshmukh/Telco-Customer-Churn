from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src import logger

def start_model_trainer():
    try:
        logger.info(">>>>> Model Training Stage started <<<<<")
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train_and_log_models()
        logger.info(">>>>> Model Training Stage completed <<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e
