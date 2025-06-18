import os
import pandas as pd
import yaml
from src.entity.data_validation_config import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate(self):
        df = pd.read_csv(self.config.data_file)

        with open(self.config.schema_file, "r") as f:
            schema = yaml.safe_load(f)

        expected_columns = schema["columns"]
        target_col = schema.get("target_column", "Churn")
        target_dtype = schema.get("target_dtype", "object")

        actual_columns = df.columns.tolist()
        expected_column_names = list(expected_columns.keys())

        missing_columns = [col for col in expected_column_names if col not in actual_columns]
        extra_columns = [col for col in actual_columns if col not in expected_column_names]

        mismatched_types = []
        for col, expected_dtype in expected_columns.items():
            if col in df.columns:
                actual_dtype = str(df[col].dtype)
                if actual_dtype != expected_dtype:
                    mismatched_types.append((col, expected_dtype, actual_dtype))

        target_mismatch = (
            target_col not in df.columns or
            str(df[target_col].dtype) != target_dtype
        )

        os.makedirs(self.config.root_dir, exist_ok=True)

        with open(self.config.status_file, "w") as f:
            if missing_columns or extra_columns or mismatched_types or target_mismatch:
                f.write("Validation Failed\n")
                if missing_columns:
                    f.write(f"Missing columns: {missing_columns}\n")
                if extra_columns:
                    f.write(f"Extra columns: {extra_columns}\n")
                if mismatched_types:
                    f.write("Mismatched data types:\n")
                    for col, expected, actual in mismatched_types:
                        f.write(f"  - {col}: expected {expected}, got {actual}\n")
                if target_mismatch:
                    f.write(f"Target column '{target_col}' is missing or of wrong dtype\n")
            else:
                f.write("Validation Successful\n")
