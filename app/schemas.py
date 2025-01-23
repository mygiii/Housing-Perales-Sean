from pydantic import BaseModel

# Ce modèle est utilisé pour la réponse GET
class House(BaseModel):
    id: int
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float
    median_house_value: float
    ocean_proximity: str

    class Config:
        orm_mode = True

# Ce modèle est utilisé pour valider les données POST
class HouseCreate(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float
    median_house_value: float
    ocean_proximity: str
