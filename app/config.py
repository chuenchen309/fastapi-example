import os
from functools import lru_cache
from typing import Literal, Optional
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings
from app.utils.logger import logger

PRIVATE_KEYS = ["XXX_API_KEY"]

class Settings(BaseSettings):
    """Time Zone"""
    DEFAULT_TIMEZONE: str = Field("Asia/Taipei", env="DEFAULT_TIMEZONE")
    """Baseic Setting"""
    APP_NAME: str = Field("fastapi-example-api", env="APP_NAME")
    APP_VERSION: str = Field("1.0.1", env="APP_VERSION")
    APP_API_URL: str = Field("http://localhost:5000", env="APP_API_URL")
    APP_UI_URL: str = Field("http://localhost:8080", env="APP_UI_URL")
    IS_TLS_ENABLE: bool = Field(True, env="IS_TLS_ENABLE")
    """MongoDB"""
    MDB_PREFIX: Optional[str] = Field(None, env="MDB_PREFIX")
    MONGODB_URL: Optional[str] = Field(None, env="MONGODB_URL")
    MONGODB_DATABASE: Optional[str] = Field(None, env="MONGODB_DATABASE")
    MONGODB_USERNAME: Optional[str] = Field(None, env="MONGODB_USERNAME")
    MONGODB_PASSWORD: Optional[str] = Field(None, env="MONGODB_PASSWORD")
    MONGODB_PASSWORD_FILE: Optional[str] = Field(None, env="MONGODB_PASSWORD_FILE")
    MONGODB_AUTH_SOURCE: Optional[str] = Field(None, env="MONGODB_AUTH_SOURCE")
    MONGODB_AUTHMECHANISM: Optional[str] = Field("SCRAM-SHA-1", env="MONGODB_AUTHMECHANISM")
    """MongoDB Collection"""
    MDB_TEMPLATE: Optional[str] = Field("template", env="MDB_TEMPLATE")

    class Config:
        env_file = ".env"

class Config(Settings):

    def __init__(self):
        super().__init__()
        self.setup_environment()

    def setup_environment(self):
        if self.MONGODB_PASSWORD is None and self.MONGODB_PASSWORD_FILE is not None:
            existence = os.path.exists(self.MONGODB_PASSWORD_FILE)
            if existence:
                with open(self.MONGODB_PASSWORD_FILE) as f:
                    self.MONGODB_PASSWORD = f.read().rstrip('\n')

@lru_cache()
def get_configs():
    configs = Config()
    config_vars = vars(configs)
    for key, value in config_vars.items():
        if key.isupper() and key not in PRIVATE_KEYS and value is not None:
            logger.debug(f"{key} ok ... : {value}")

    return configs

configs = get_configs()
