from fastapi import APIRouter

from property import schemas
from property.repository import apartment

router = APIRouter(
    prefix='/apartment',
    tags=['apartment']
)


@router.post('/')
async def predict(request: schemas.Apartment):
    """
    Endpoint to predict the price of an apartment.

    Args:
        request (schemas.Apartment): The request payload containing the details of the apartment.

    Returns:
        dict: A dictionary containing the predicted price of the apartment.
    """
    return apartment.predict_apartment_price(request)
