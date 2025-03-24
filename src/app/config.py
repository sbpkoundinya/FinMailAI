import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    openai_model: str = "gpt-4"
    snow_instance: str
    snow_username: str
    snow_password: str
    
    class Config:
        env_file = ".env"

settings = Settings()