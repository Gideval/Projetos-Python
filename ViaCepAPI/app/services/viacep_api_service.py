from app.models.responses.viacep_api_response import ViaCepResponse
from app.facades.viacep_api_facade import ViaCepAPIFacade

class ViaCepAPIService:
    def __init__(self):
        self.facade = ViaCepAPIFacade()

    async def get_address_by_zipCode(self, zipCode: str) -> ViaCepResponse:
        return await self.facade.fetch_cep_data(zipCode)

    async def get_address_by_location(self, uf: str, city: str, street: str) -> ViaCepResponse:
        return await self.facade.fecth_address_data(uf, city, street)