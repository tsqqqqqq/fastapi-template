from functools import lru_cache

from config.Conf import Settings


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
