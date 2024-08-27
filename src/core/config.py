import functools
import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.prod", env_file_encoding="utf-8")

    root_dir: str = os.path.abspath(__file__ + 3 * "/..")
    src_dir: str = os.path.join(root_dir, "src")

    PROJECT_NAME: str = "open-chat"
    RELOAD: bool = True

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8888

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

@functools.lru_cache()
def settings():
    return Settings()