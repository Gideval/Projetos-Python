from app.facades.pokeapi_facade import PokeAPIFacade

class PokemonService:
    def __init__(self):
        self.facade = PokeAPIFacade()

    async def get_formatted_pokemon(self, name: str) -> dict:
        raw_data = await self.facade.fetch_raw_data(name)

        return {
            "name": raw_data["name"].capitalize(),
            "id": raw_data["id"],
            "abilities": [h["ability"]["name"] for h in raw_data["abilities"]]

        }