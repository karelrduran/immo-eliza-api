from pydantic import BaseModel, field_validator

provinces = ['ANTWERPEN', 'BRUSSEL', 'HENEGOUWEN', 'LIMBURG', 'LUIK', 'LUXEMBURG', 'NAMEN', 'OOST-VLAANDEREN',
             'VLAAMS-BRABANT', 'WAALS-BRABANT', 'WEST-VLAANDEREN']


class Province(BaseModel):
    """
    Pydantic model for representing provinces.

    Attributes:
        name (str): The name of the province.
    """
    name: str

    @field_validator('name')
    @classmethod
    def validate_province(cls, v: str):
        """
        Validates the province name against a predefined list of valid province names.

        Args:
            v (str): The province name to be validated.

        Raises:
            ValueError: If the provided province name is not in the list of valid provinces.

        Returns:
            str: The validated province name.
        """
        if v.upper() not in provinces:
            raise ValueError(f"{v} is no a valid province")
        return v


class Property(BaseModel):
    """
    Pydantic base model for properties.

    Attributes:
        facades (int): Number of facades.
        habitable_surface (float): Habitable surface area.
        bedroom_count (int, optional): Number of bedrooms. Defaults to 0.
        bathroom_count (int, optional): Number of bathrooms. Defaults to 0.
        toilet_count (int, optional): Number of toilets. Defaults to 0.
        room_count (int, optional): Number of rooms. Defaults to 0.
        kitchen_type (str | int): Type of kitchen.
        furnished (bool | int, optional): Indicates if the property is furnished. Defaults to False.
        terrace (bool | int, optional): Indicates if the property has a terrace. Defaults to False.
        garden_exists (bool | int, optional): Indicates if the property has a garden. Defaults to False.
        state_of_building (str | int): State of the building.
        living_surface (float): Living surface area.
        epc (str | int): Energy Performance Certificate (EPC) value.
        consumption_per_m2 (float): Energy consumption per square meter.
        province (Province): The province where the property is located.
    """
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
    """
    Pydantic model for representing houses, inheriting from Property model.

    Attributes:
        land_surface (float): Land surface area.
    """
    land_surface: float


class Apartment(Property):
    """
    Pydantic model for representing apartments, inheriting from Property model.

    Attributes:
        terrace_surface (float): Terrace surface area.
    """
    terrace_surface: float


class Prediction(BaseModel):
    """
    Pydantic model for representing predictions.

    Attributes:
        prediction (float): The predicted value.
    """
    prediction: float
