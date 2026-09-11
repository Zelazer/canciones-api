from fastapi import FastAPI

from app.routers.canciones import router

app = FastAPI(
    title="API de Canciones",
    description="API para guardar canciones",
    version="1.0.0"
)

app.include_router(router)