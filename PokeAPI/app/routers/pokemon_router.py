from fastapi import APIRouter, Depends
from app.services.pokemon_service import PokemonService

router = APIRouter(prefix="/pokemon", tags=["Pokemons"])

@router.get("/{name}")
async def get_pokemon(name: str, service: PokemonService = Depends()):
    return await service.get_formatted_pokemon(name)