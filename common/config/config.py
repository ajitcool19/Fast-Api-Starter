from functools import lru_cache

from pydantic_settings import BaseSettings


class Dev(BaseSettings):
    DEBUG: bool = True
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///dev-site.db'


@lru_cache()
def get_config_based_on_environment():
    from common.environment import get_env

    env = get_env()

    if env == 'dev':
        return Dev()
    return Dev()


current_config = get_config_based_on_environment()