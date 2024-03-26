from pydantic import BaseModel, field_validator

provinces = ['ANTWERPEN', 'BRUSSEL', 'HENEGOUWEN', 'LIMBURG', 'LUIK', 'LUXEMBURG', 'NAMEN', 'OOST-VLAANDEREN',
             'VLAAMS-BRABANT', 'WAALS-BRABANT', 'WEST-VLAANDEREN']


class Province(BaseModel):
    name: str

    @field_validator('name')
    @classmethod
    def validate_province(cls, v: str):
        if v.upper() not in provinces:
            raise ValueError(f"{v} is no a valid province")
        return v


class Property(BaseModel):
    facades: int
    habitable_surface: float
    bedroom_count: int = 0
    bathroom_count: int = 0
    toilet_count: int = 0
    room_count: int = 0
    kitchen_type: str | int
    furnished: bool | int = False
    terrace: bool | int = False
    garden_exists: bool | int = False
    state_of_building: str | int
    living_surface: float
    epc: str | int
    consumption_per_m2: float
    province: Province


class House(Property):
    land_surface: float


class Apartment(Property):
    terrace_surface: float


class Prediction(BaseModel):
    prediction: float
