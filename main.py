from fastapi import FastAPI

from property.routers import house, apartment
from config import Config

config = Config()

app = FastAPI(
    title="Price predictor for houses and apartments in Belgium",
    # summary="House and Apartment Price Predictor API",
    description=config.description,
    version="1.0.0",
    contact={
        "name": "Karel Rodriguez Duran",
        "email": "krduran@gmail.com",
        "url": "https://www.linkedin.com/in/karel-rodriguez-duran/"
    }

)

app.include_router(house.router)
app.include_router(apartment.router)

@app.get('/')
def root():
    return {"message": "It is alive!"}
