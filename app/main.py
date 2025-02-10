from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()

@app.get("/")
def root():
    return {
        "app_name": settings.app_name,
        "host": settings.host,
        "port": settings.port,
        "reload": settings.reload,
        "database_url": settings.database_url
    }
