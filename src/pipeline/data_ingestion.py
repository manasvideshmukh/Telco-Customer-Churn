from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion

def run_data_ingestion():
    config = ConfigurationManager()
    ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=ingestion_config)
    data_ingestion.ingest_data()
