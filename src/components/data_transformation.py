import os
import pandas as pd
import numpy as np
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.entity.data_transformation_config import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def initiate_data_transformation(self):
        # ✅ Ensure the output directory exists
        os.makedirs(self.config.root_dir, exist_ok=True)

        # Load data
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        # Save customer IDs if needed
        train_ids = train_df["customerID"]
        test_ids = test_df["customerID"]

        # Drop customerID (won't be used for training)
        train_df.drop(columns=["customerID"], inplace=True)
        test_df.drop(columns=["customerID"], inplace=True)

        # Split features and target
        X_train = train_df.drop(columns=["Churn"])
        y_train = train_df["Churn"]
        X_test = test_df.drop(columns=["Churn"])
        y_test = test_df["Churn"]

        # Identify columns
        numerical_cols = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()

        # Create ColumnTransformer
        transformer = ColumnTransformer(transformers=[
            ("num", StandardScaler(), numerical_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_cols)
        ])

        # Fit and transform
        X_train_transformed = transformer.fit_transform(X_train)
        X_test_transformed = transformer.transform(X_test)

        # Save transformed arrays as CSV
        pd.DataFrame(X_train_transformed).to_csv(self.config.transformed_train_path, index=False)
        pd.DataFrame(X_test_transformed).to_csv(self.config.transformed_test_path, index=False)

        # Save transformer object
        joblib.dump(transformer, self.config.transformer_object_path)
