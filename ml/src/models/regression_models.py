from xgboost import XGBRegressor

import pickle
import pandas as pd

pd.set_option('future.no_silent_downcasting', True)


class XGBoostRegression:
    """
    Class for performing predictions using an XGBoost regression model.

    Attributes:
        model (XGBRegressor): The trained XGBoost regression model.
        y_pred (numpy.ndarray): Array to store the predicted values.
    """

    def __init__(self, model_path: str = None):
        """
        Initialize XGBoostRegression class with the provided model path.

        Args:
            model_path (str, optional): Path to the trained XGBoost regression model file. Defaults to None.
        """
        self.model = self.load_model(model_path=model_path)
        self.y_pred = None

        # self.predict()

    def load_model(self, model_path: str) -> XGBRegressor:
        """
        Load the trained XGBoost regression model from the specified file path.

        Args:
            model_path (str): Path to the trained XGBoost regression model file.

        Returns:
            XGBRegressor: The loaded XGBoost regression model.
        """
        try:
            with open(model_path, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    def predict(self, new_data: pd.DataFrame = None):
        """
        Make predictions using the trained XGBoost regression model.

        Args:
            new_data (pd.DataFrame, optional): DataFrame containing the new data for prediction. Defaults to None.
        """
        self.y_pred = self.model.predict(new_data)
