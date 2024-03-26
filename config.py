import os


class Config:
    def __init__(self):
        # Get project dir path
        self.project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        self.ap_trained_model = os.path.join(self.project_dir, 'ml', 'models', 'ap_xgboost_reg.pkl')
        self.h_trained_model = os.path.join(self.project_dir, 'ml', 'models', 'h_xgboost_reg.pkl')
        self.description = """
    This API provides a service to predict the selling price of houses and apartments based on a set of provided features in JSON format. It utilizes an XGBoost regression model to generate the predictions.
    
    JSON format for houses:
    {
        "facades": int,
        "habitable_surface": float,
        "bedroom_count": int,
        "bathroom_count": int,
        "toilet_count": int,
        "room_count": int,
        "kitchen_type": "string",
        "furnished": bool,
        "terrace": bool,
        "garden_exists": bool,
        "state_of_building": "string",
        "living_surface": float,
        "epc": "string",
        "consumption_per_m2": float,
        "province": {
            "name": "string"
        },
        "land_surface": float
    }

    JSON format for apartments:
    {
        "facades": int,
        "habitable_surface": float,
        "bedroom_count": int,
        "bathroom_count": int,
        "toilet_count": int,
        "room_count": int,
        "kitchen_type": "string",
        "furnished": bool,
        "terrace": bool,
        "garden_exists": bool,
        "state_of_building": "string",
        "living_surface": float,
        "epc": "string",
        "consumption_per_m2": float,
        "province": {
            "name": "string"
        },
        "terrace_surface": float
    }

    The API returns the predicted price as a JSON object with the following structure:
    {
        "predicted_price": int
    }

    To make predictions, the API uses a pre-trained XGBoost regression model with historical data of house and apartment prices. The specific parameters provided in the JSON are used as input features for the model, and an estimate of the price is generated based on these features.
    """
