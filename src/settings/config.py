import logging

from typing import List
from pydantic import BaseSettings as PydanticBaseSettings


class BaseConfig(PydanticBaseSettings):
    """Base configuration"""
    app_name: str = "user registration API"
    app_version: str = "0.1.0-alpha"
    app_description: str = "user registration REST API"

    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"

    database_url: str

    jwt_secret: str
    secret_key: str = "change me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    activation_token_expire_seconds: int = 3600
    testing: bool = False
    suppress_mail_send: int = 0

    mail_username: str = "yourusername"
    mail_password: str = "strong_password"
    mail_from: str = "your@email.com"
    mail_port: int = 587
    mail_server: str = "your mail server"
    mail_from_name: str = "desired name"
    mail_tls: bool = True
    mail_ssl: bool = False
    use_credentials: bool = True
    validate_certs: bool = True

    class Config:
        env_file = ".env"


class DevConfig(BaseConfig):
    """Dev configuration"""
    log_level: int = logging.DEBUG


class TestConfig(BaseConfig):
    """Test configuration"""
    database_test_url: str
    testing: bool = True
    suppress_mail_send: int = 1
    activation_token_expire_seconds: int = 1


class ProdConfig(BaseConfig):
    """Production configuration"""
    env: str = "PRODUCTION"
    app_name: str = "user registration Production API"


class EnvConfig(PydanticBaseSettings):
    environment: str = None

    def load_config(self):
        if self.environment == "PROD":
            return ProdConfig()
        if self.environment == "TEST":
            return TestConfig()
        return DevConfig()
    

env_config = EnvConfig()
configurations = env_config.load_config()
