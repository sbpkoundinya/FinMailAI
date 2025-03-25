import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Required
    openai_api_key: str
    snow_instance: str
    snow_username: str
    snow_password: str
    
    # Optional with defaults
    max_file_size_mb: int = 25
    debug: bool = False
    
    class Config:
        env_file = ".env"

settings = Settings()