import httpx
from fastapi import HTTPException
from app.models.responses.viacep_api_response import ViaCepResponse

class ViaCepAPIFacade:
    def __init__(self):
        self.url_base = "https://viacep.com.br/ws/"

    async def fetch_cep_data(self, zipCode: str) -> ViaCepResponse:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.url_base}{zipCode}/json/")
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError:
                raise HTTPException(satus_code=404, detail="Address not found")

    async def fecth_address_data(self, uf: str, city: str, street: str) -> ViaCepResponse:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.url_base}/{uf}/{city}/{street}/json/")
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError:
                raise HTTPException(satus_code=404, detail="Address not found")