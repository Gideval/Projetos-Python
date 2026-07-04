import httpx
from fastapi import HTTPException

class PokeAPIFacade:
    def __init__(self):
        self.url_base = "https://pokeapi.co/api/v2/pokemon/"

    async def fetch_raw_data(self, name: str) -> dict:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.url_base}{name.lower()}")
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError:
                raise HTTPException(status_code=404, detail="Not found in PokeAPI")