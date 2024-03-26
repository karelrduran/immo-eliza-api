from xgboost import XGBRegressor

import pickle
import pandas as pd

pd.set_option('future.no_silent_downcasting', True)


class XGBoostRegression:
    def __init__(self, model_path: str = None):
        self.model = self.load_model(model_path=model_path)
        self.y_pred = None

        # self.predict()

    def load_model(self, model_path: str) -> XGBRegressor:
        try:
             with open(model_path, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    def predict(self, new_data: pd.DataFrame = None):
        """Make predictions using the trained model."""
        self.y_pred = self.model.predict(new_data)
