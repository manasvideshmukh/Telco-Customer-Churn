from src.pipeline.data_ingestion import run_data_ingestion
from src.pipeline.data_transformation_pipeline import start_data_transformation
from src.pipeline.data_validation_pipeline import start_data_validation
from src.pipeline.model_trainer_pipeline import start_model_trainer

if __name__ == "__main__":
    run_data_ingestion()
    start_data_transformation()
    start_data_validation()
    start_model_trainer()