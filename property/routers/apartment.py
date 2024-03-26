from fastapi import APIRouter

from property import schemas
from property.repository import apartment

router = APIRouter(
    prefix='/apartment',
    tags=['apartment']
)


@router.post('/')
async def predict(request: schemas.Apartment):
    return apartment.predict_apartment_price(request)
