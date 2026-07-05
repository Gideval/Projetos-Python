from app.models.responses.openMeteo.open_meteo_api_response import OpenMeteoApiResponse
from app.facades.openMeteo.open_meteo_api_facade import OpenMeteoAPIFacade
from app.services.geocoding.geocoding_api_service import GeocodingAPIService

class OpemMeteoAPIService:
    def __init__(self):
        self.facade = OpenMeteoAPIFacade()
        self.service = GeocodingAPIService()

    async def get_current_weather(self, city: str) -> OpenMeteoApiResponse:
        responseCoordinates = await self.service.get_coordinates(city)

        latitude = responseCoordinates.results[0].latitude
        longitude = responseCoordinates.results[0].longitude

        return await self.facade.fetch_current_weather(latitude, longitude)
