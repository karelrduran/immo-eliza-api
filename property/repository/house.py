from property import schemas
from ml.src.data.data_transformation import Transformation
from ml.src.models.regression_models import XGBoostRegression
from config import Config

config = Config()


def predict_house_price(house: schemas.House):
    """
    Predicts the price of a house using the provided house details.

    Args:
        house (schemas.House): The details of the house for which the price is to be predicted.

    Returns:
        dict: A dictionary containing the predicted price of the house.
    """
    data = Transformation.transform(house, property_type='house')
    regressor = XGBoostRegression(model_path=config.h_trained_model)
    regressor.predict(new_data=data)
    print(regressor.y_pred[0])

    return {'predicted_price': round(float(regressor.y_pred[0]), 2)}
