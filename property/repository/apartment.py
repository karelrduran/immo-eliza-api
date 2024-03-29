from property import schemas
from ml.src.data.data_transformation import Transformation
from ml.src.models.regression_models import XGBoostRegression
from config import Config

config = Config()


def predict_apartment_price(apartment: schemas.Apartment):
    """
    Predicts the price of an apartment using the provided apartment details.

    Args:
        apartment (schemas.Apartment): The details of the apartment for which the price is to be predicted.

    Returns:
        dict: A dictionary containing the predicted price of the apartment.
    """
    data = Transformation.transform(apartment, property_type='apartment')
    regressor = XGBoostRegression(model_path=config.ap_trained_model)
    regressor.predict(new_data=data)
    print(regressor.y_pred[0])

    return {'predicted_price': round(float(regressor.y_pred[0]), 2)}
