from pydantic import BaseModel

class GeocodingApiResultResponse(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    elevation: float
    country: str
    admin1: str