from pydantic import BaseModel

class OpenMeteoApiResultResponse(BaseModel):
    time: str
    temperature_2m: float
    relative_humidity: int
    wind_speed_10m: float