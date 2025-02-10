from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Project"
    host: str = "0.0.0.0"
    port: int = 8000

settings = Settings()
