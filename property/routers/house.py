from fastapi import APIRouter

from property import schemas
from property.repository import house

router = APIRouter(
    prefix='/house',
    tags=['house']
)


@router.post('/')
async def predict(request: schemas.House):
    return house.predict_house_price(request)
