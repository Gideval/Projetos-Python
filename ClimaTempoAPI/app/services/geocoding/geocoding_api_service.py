from app.models.responses.geocoding.geocoding_api_response import GeocodingApiResponse
from app.facades.geocoding.geocoding_api_facade import GeocodingAPIFacade

class GeocodingAPIService:
    def __init__(self):
        self.facade = GeocodingAPIFacade()

    async def get_coordinates(self, city: str) -> GeocodingApiResponse:
        return await self.facade.fetch_coordinate(city)