from fastapi import APIRouter, Depends
from app.services.viacep_api_service import ViaCepAPIService

router = APIRouter(prefix="/viacep", tags=["ViaCEP"])

@router.get("/cep/{zip_code}")
async def get_address_by_zipCode(zip_code: str, service: ViaCepAPIService = Depends()):
    return await service.get_address_by_zipCode(zip_code)

@router.get("/address")
async def get_address_by_address(uf: str, city: str, street: str, service: ViaCepAPIService = Depends()):
    return await service.get_address_by_location(uf, city, street)