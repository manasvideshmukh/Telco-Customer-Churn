import os
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from src.entity.model_trainer_config import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    import os
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from src.entity.model_trainer_config import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_and_log_models(self):
        # Load features
        X_train = pd.read_csv(self.config.transformed_train_path)
        X_test = pd.read_csv(self.config.transformed_test_path)

        # Load target separately from original CSVs
        y_train = pd.read_csv(self.config.train_data_path)[self.config.target_column]
        y_test = pd.read_csv(self.config.test_data_path)[self.config.target_column]

        # ✅ Encode target: "Yes" → 1, "No" → 0
        y_train = y_train.map({"Yes": 1, "No": 0})
        y_test = y_test.map({"Yes": 1, "No": 0})

        os.makedirs(self.config.root_dir, exist_ok=True)

        # Start MLflow experiment
        mlflow.set_experiment("Churn Model Comparison")

        models = {
            "LogisticRegression": LogisticRegression(**self.config.logistic_regression),
            "RandomForest": RandomForestClassifier(**self.config.random_forest),
            "XGBoost": XGBClassifier(**self.config.xgboost)
        }

        for name, model in models.items():
            with mlflow.start_run(run_name=name):
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                # Log model
                mlflow.sklearn.log_model(model, name)
                mlflow.log_params(model.get_params())

                # Log metrics safely
                report = classification_report(y_test, y_pred, output_dict=True)
                labels = [lbl for lbl in report.keys() if lbl not in ("accuracy", "macro avg", "weighted avg")]
                label = labels[0] if labels else "1"

                mlflow.log_metrics({
                    "accuracy": report.get("accuracy", 0),
                    "precision": report.get(label, {}).get("precision", 0),
                    "recall": report.get(label, {}).get("recall", 0),
                    "f1_score": report.get(label, {}).get("f1-score", 0)
                })

        # Save the last model
        joblib.dump(model, self.config.model_path)
