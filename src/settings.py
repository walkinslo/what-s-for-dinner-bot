from functools import cache
from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


@cache
def get_env_path() -> Path | None:
    if Path.exists(BASE_DIR / ".env"):
        return BASE_DIR / ".env"
    else:
        print("No .env file was found!")


class Settings(BaseSettings):
    """Настройки бота."""

    BOT_TOKEN: str # токен Telegram Bot Api

    class Config:
        env_file = get_env_path()


@cache
def get_settings():
    return Settings()


settings = get_settings()