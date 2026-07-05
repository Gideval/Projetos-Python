from pydantic import BaseModel
from app.models.responses.openMeteo.open_meteo_api_result_response import OpenMeteoApiResultResponse

class OpenMeteoApiResponse(BaseModel):
    current: OpenMeteoApiResultResponse