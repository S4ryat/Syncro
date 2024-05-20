import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

print("POSTGRES_SERVER:", os.getenv("POSTGRES_SERVER"))
print("POSTGRES_USER:", os.getenv("POSTGRES_USER"))
print("POSTGRES_PASSWORD:", os.getenv("POSTGRES_PASSWORD"))
print("POSTGRES_DB:", os.getenv("POSTGRES_DB"))


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        env_file = "../.env"


settings = Settings()
