from pydantic import BaseModel
from app.models.responses.geocoding.geocoding_api_result_response import GeocodingApiResultResponse

class GeocodingApiResponse(BaseModel):
    results: list[GeocodingApiResultResponse]