from property import schemas
from ml.src.data.data_transformation import Transformation
from ml.src.models.regression_models import XGBoostRegression
from config import Config

config = Config()


def predict_house_price(house: schemas.House):
    data = Transformation.transform(house, property_type='house')
    regressor = XGBoostRegression(model_path=config.h_trained_model)
    regressor.predict(new_data=data)
    print(regressor.y_pred[0])

    return {'predicted_price': float(regressor.y_pred[0])}
