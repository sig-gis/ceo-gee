from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    host: str
    port: int
    debug: bool
    reload: bool
    gee_service_account: str
    gee_private_key_path: str
    class Config:
        env_file = ".env"

settings = Settings()
