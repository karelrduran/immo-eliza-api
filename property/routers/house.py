from fastapi import APIRouter

from property import schemas
from property.repository import house

router = APIRouter(
    prefix='/house',
    tags=['house']
)


@router.post('/')
async def predict(request: schemas.House):
    """
    Endpoint to predict the price of a house.

    Args:
        request (schemas.House): The request payload containing the details of the house.

    Returns:
        dict: A dictionary containing the predicted price of the house.
    """
    return house.predict_house_price(request)
