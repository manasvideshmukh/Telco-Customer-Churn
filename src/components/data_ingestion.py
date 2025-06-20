import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.entity.data_ingestion_config import DataIngestionConfig
from src import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def ingest_data(self):
        os.makedirs(self.config.root_dir, exist_ok=True)
        
        df = pd.read_csv(self.config.source_file)

        # ✅ Fix TotalCharges dtype
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
        df["TotalCharges"] = df["TotalCharges"].fillna(0)

        df.to_csv(self.config.raw_data, index=False)

        train_df, test_df = train_test_split(
            df,
            test_size=self.config.test_size,
            random_state=self.config.random_state
        )

        train_df.to_csv(self.config.train_data, index=False)
        test_df.to_csv(self.config.test_data, index=False)

        logger.info(f"Train shape: {train_df.shape}, Test shape: {test_df.shape}")
