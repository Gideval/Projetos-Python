import httpx
from fastapi import HTTPException
from app.models.responses.geocoding.geocoding_api_response import GeocodingApiResponse

class GeocodingAPIFacade:
    def __init__(self):
        self.url_base = "https://geocoding-api.open-meteo.com/v1/search?name="

    async def fetch_coordinate(self, city: str) -> GeocodingApiResponse:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.url_base}{city}&count=1&language=pt&format=json")
                response.raise_for_status()
                return GeocodingApiResponse(**response.json())
            except httpx.HTTPStatusError:
                raise HTTPException(satus_code=404, detail="Address not found")