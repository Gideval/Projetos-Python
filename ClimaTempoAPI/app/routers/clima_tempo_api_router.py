from fastapi import APIRouter, Depends
from app.services.openMeteo.open_meteo_api_service import OpemMeteoAPIService

router = APIRouter(prefix="/clima/tempo", tags=["Clima"])

@router.get("/weather/{city}")
async def get_current_weather(city: str, service: OpemMeteoAPIService = Depends()):
    return await service.get_current_weather(city)