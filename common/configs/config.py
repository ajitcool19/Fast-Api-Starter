from functools import lru_cache

from pydantic_settings import BaseSettings


class Dev(BaseSettings):
    DEBUG: bool = True
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///dev-site.db'

    # Sentry
    SENTRY_DSN: str = 'dsn'

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    TRACES_SAMPLE_RATE: float = 20.0
    PROFILES_SAMPLE_RATE: float = 20.0

    # Jwt
    JWT_SECRET: str = 'secret'
    JWT_EXPIRATION_TIME: int = 360000

    # Middlewares
    MIDDLEWARES: list = ["login","db_session","timer","auth"]



@lru_cache()
def get_config_based_on_environment():
    from common.environment import get_env

    env = get_env()

    if env == 'dev':
        return Dev()
    return Dev()


current_config = get_config_based_on_environment()
