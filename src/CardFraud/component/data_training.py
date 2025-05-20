from typing import Dict, Tuple
import pandas as pd
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from exception import CustomException
from logger import logging
import sys
import joblib
from sklearn.model_selection import RandomizedSearchCV
from CardFraud.config.configuration import DataTrainingConfig




class ModelTraining:
    def __init__(self, config: DataTrainingConfig):
        self.config = config

    def load_data(self, trainpath: Path, testpath: Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
        try:
            train = pd.read_csv(trainpath)
            test = pd.read_csv(testpath)
            logging.info(f"Data loaded successfully from {trainpath} and {testpath}")
            return train, test
        except Exception as e:
            raise CustomException(e, sys)

    def split_data(self, train_data: pd.DataFrame, test_data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
        try:
            X_train = train_data.drop("Class", axis=1)
            y_train = train_data["Class"]
            X_test = test_data.drop("Class", axis=1)
            y_test = test_data["Class"]
            logging.info("Data split successfully")
            return X_train, y_train, X_test, y_test
        except Exception as e:
            raise CustomException(e, sys)

    def get_models(self) -> Dict[str, object]:
        """Define the models to be trained."""
        models = {
            "LogisticRegression": LogisticRegression(),
            "RandomForest": RandomForestClassifier(),
            "DecisionTree": DecisionTreeClassifier(),
            "XGBoost": xgb.XGBClassifier()
        }
        return models

    def get_params(self) -> Dict[str, dict]:
        """Fetch parameters from the configuration."""
        param_grid = {
            "LogisticRegression": {
                "C": [0.1, 1],
                "solver": ["liblinear"],
                "max_iter": [100, 200]
            },
            "RandomForest": {
                "n_estimators": self.config.n_estimators,
                "max_depth": self.config.max_depth,
                "min_samples_split": self.config.min_samples_split,
                "min_samples_leaf": self.config.min_samples_leaf,
                "max_features": self.config.max_features
            },
            "DecisionTree": {
                "max_depth": self.config.max_depth,
                "min_samples_split": self.config.min_samples_split,
                "min_samples_leaf": self.config.min_samples_leaf,
                "max_features": self.config.max_features
            },
            "XGBoost": {
                "n_estimators": self.config.n_estimators,
                "learning_rate": self.config.learning_rate,
                "max_depth": self.config.max_depth
            }
        }
        return param_grid



    # def training(self, X_train: pd.DataFrame, y_train: pd.Series) -> Dict[str, object]:
    #     """Train the models using randomized search with parameters defined in the config."""
    #     models = self.get_models()
    #     param_grid = self.get_params()
    #     trained_models = {}

    #     # for model_name, model in models.items():
    #     #     try:
        #         logging.info(f"Training {model_name} with RandomizedSearchCV...")

        #         # Calculate total combinations
        #         grid = param_grid[model_name]
        #         total_combinations = 1
        #         for v in grid.values():
        #             total_combinations *= len(v)

        #         n_iter = min(5, total_combinations)

        #         random_search = RandomizedSearchCV(
        #             estimator=model,
        #             param_distributions=grid,
        #             n_iter=n_iter,
        #             cv=2,
        #             scoring='f1',
        #             n_jobs=2,
        #             verbose=1,
        #             random_state=42
        #         )

        #         random_search.fit(X_train, y_train)
        #         trained_models[model_name] = random_search.best_estimator_

        #     except Exception as e:
        #         raise CustomException(e, sys)

    def training(self, X_train: pd.DataFrame, y_train: pd.Series) -> Dict[str, object]:
        """Train the models directly without hyperparameter search."""
        models = self.get_models()
        trained_models = {}

        for model_name, model in models.items():
            try:
                logging.info(f"Training {model_name} with default parameters...")
                model.fit(X_train, y_train)
                trained_models[model_name] = model
            except Exception as e:
                raise CustomException(e, sys)

        logging.info("Model training completed successfully without hyperparameter tuning.")
        return trained_models
        # logging.info("Model training completed successfully with RandomizedSearchCV")
        # return trained_models


    def evaluate_models(self, models: Dict[str, object], X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
        """Evaluate the models and return a DataFrame of metrics."""
        metrics_list = []

        for model_name, model in models.items():
            try:
                y_pred = model.predict(X_test)
                
                accuracy = accuracy_score(y_test, y_pred)
                precision = precision_score(y_test, y_pred, zero_division=1)
                recall = recall_score(y_test, y_pred, zero_division=1)
                f1 = f1_score(y_test, y_pred, zero_division=1)

                metrics_list.append({
                    "Model": model_name,
                    "Accuracy": accuracy,
                    "Precision": precision,
                    "Recall": recall,
                    "F1 Score": f1
                })

            except Exception as e:
                raise CustomException(e, sys)

        metrics_df = pd.DataFrame(metrics_list)
        logging.info(f"Evaluation Metrics:\n{metrics_df}")
        return metrics_df

    def select_best_model(self, metrics_df: pd.DataFrame) -> str:
        """Select the best model based on F1 Score."""
        try:
            best_model_row = metrics_df.loc[metrics_df["F1 Score"].idxmax()]
            best_model_name = best_model_row["Model"]
            logging.info(f"Best Model: {best_model_name} with F1 Score: {best_model_row['F1 Score']}")
            return best_model_name
        except Exception as e:
            raise CustomException(e, sys)
        
        
    
    def save_best_model(self, best_model_name: str, trained_models: Dict[str, object]) -> None:
            # """Save the best model to a .pkl file."""
        try:
            best_model = trained_models[best_model_name]
            
            # Ensure the model directory exists
            os.makedirs(self.config.model_dir, exist_ok=True)
            
            # Save the best model to the specified path
            joblib.dump(best_model, self.config.model_pkl_file)
            logging.info(f"Best model '{best_model_name}' saved to {self.config.model_pkl_file}")

        except Exception as e:
            raise CustomException(e, sys)
        
        
        
        
        
        
    def run_training_pipeline(self) -> pd.DataFrame:
            # """
            # Run the full training pipeline: load data, train models, evaluate them,
            # select the best model, and save it as a .pkl file.
            # """
        try:
            # 1. Load data
            train_df, test_df = self.load_data(self.config.processed_train_path, self.config.processed_test_path)

            # 2. Split data
            X_train, y_train, X_test, y_test = self.split_data(train_df, test_df)

            # 3. Train models
            trained_models = self.training(X_train, y_train)

            # 4. Evaluate models
            metrics_df = self.evaluate_models(trained_models, X_test, y_test)

            # 5. Select the best model
            best_model_name = self.select_best_model(metrics_df)

            # 6. Save the best model
            self.save_best_model(best_model_name, trained_models)

            logging.info("Training pipeline completed successfully.")
            return metrics_df

        except Exception as e:
            raise CustomException(e, sys)

