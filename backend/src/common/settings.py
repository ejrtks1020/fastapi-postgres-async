from functools import lru_cache

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
import os

PROFILE = os.getenv("PROFILE", "local")

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str
    POSTGRES_URL: PostgresDsn
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATE_FORMAT: str

    class Config:
        # env_file = f'../env/.env.{PROFILE}'
        env_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), f"env/.env.{PROFILE}"
        )
        env_file_encoding = "utf-8"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
