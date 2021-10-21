from pydantic import BaseSettings, Field
from functools import lru_cache

class Settings(BaseSettings):
    # Application
    api_version: str
    log_level: str


@lru_cache(maxsize=50)
def get_settings():
    return Settings(_env_file="./env/dev.env")


get_settings.cache_clear()
