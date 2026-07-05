from fastapi import FastAPI
from app.routers.clima_tempo_api_router import router as clima_router

app = FastAPI()

app.include_router(clima_router)