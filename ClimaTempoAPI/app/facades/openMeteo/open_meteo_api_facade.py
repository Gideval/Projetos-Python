import httpx
from fastapi import HTTPException
from app.models.responses.openMeteo.open_meteo_api_response import OpenMeteoApiResponse

class OpenMeteoAPIFacade:
    def __init__(self):
        self.url_base = "https://api.open-meteo.com/v1/forecast?"

    async def fetch_current_weather(self, latitude: float, longitude: float) -> OpenMeteoApiResponse:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.url_base}latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m")
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError:
                raise HTTPException(satus_code=404, detail="Address not found")