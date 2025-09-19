from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "employee_db"
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")  # Use 'localhost' for local dev, override to 'db' in Docker
    POSTGRES_PORT: int = 5432
    DATABASE_URL: Optional[str] = None  # Allow DATABASE_URL from .env

    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change_me")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "change_me")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        user = self.POSTGRES_USER
        pwd = self.POSTGRES_PASSWORD
        host = self.POSTGRES_HOST
        port = self.POSTGRES_PORT
        db = self.POSTGRES_DB
        return f"postgresql://{user}:{pwd}@{host}:{port}/{db}"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }

settings = Settings()