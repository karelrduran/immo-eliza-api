from property import schemas
from ml.src.data.data_transformation import Transformation
from ml.src.models.regression_models import XGBoostRegression
from config import Config

config = Config()


def predict_apartment_price(apartment: schemas.Apartment):
    data = Transformation.transform(apartment, property_type='apartment')
    regressor = XGBoostRegression(model_path=config.ap_trained_model)
    regressor.predict(new_data=data)
    print(regressor.y_pred[0])

    return {'predicted_price': float(regressor.y_pred[0])}
