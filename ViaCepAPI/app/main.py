from fastapi import FastAPI
from app.routers.viacep_api_router import router as viacep_router

app = FastAPI()

app.include_router(viacep_router)