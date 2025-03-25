import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

class Settings(BaseSettings):
    # Required
    openai_api_key: str
    snow_instance: str
    snow_username: str
    snow_password: str
    openai_model: str = "gpt-3.5-turbo"
    
    # Optional with defaults
    max_file_size_mb: int = 25
    debug: bool = False
    
    class Config:
        env_file = ".env"

settings = Settings()