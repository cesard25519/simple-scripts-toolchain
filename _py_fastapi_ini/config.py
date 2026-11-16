from typing import NamedTuple, Self


class Namespace(NamedTuple):
    settings: str
    utils: str
    mod: str


    @classmethod
    def as_fold(cls) -> Self:
        return cls(
            settings=settings,
            utils=utils,
            mod=mod,
        )


mod: str = """from .settings import Settings


SETTINGS: Settings = Settings()
"""

utils: str = """
"""

settings: str = '''from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict

from pyseto import Key, KeyInterface


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_file='.env',
    )

    TOKEN_KEY_EXPIRE_TIME: int
    TOKEN_KEY: str

    DEBUG: bool
    PORT: int
    HOST: str


    DATABASE_AUTH_TOKEN: str
    DATABASE_DSN: str = ''
    DATABASE_URL: str
    """
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PORT: int
    DATABASE_MAX: int


    @property
    def DATABASE_DSN(self) -> str:
        return (
            f'postgresql://{ self.DATABASE_USER }:'
            f'{ self.DATABASE_PASSWORD }'
            f'@{ self.DATABASE_HOST }:{self.DATABASE_PORT}/{self.DATABASE_NAME}'
        )

    # @property
    # def DATABASE_URL(self) -> str: return '...'
    @property
    def DATABASE_URL(self) -> str:
        return (
            f'postgresql+psycopg2://{ self.DATABASE_USER }:'
            f'{ self.DATABASE_PASSWORD }'
            f'@{ self.DATABASE_HOST }:{ self.DATABASE_PORT }/{ self.DATABASE_NAME }'
        )

    """

    @cached_property
    def KEY_INTERFACE(self) -> KeyInterface:
        return Key.new(
            key=self.TOKEN_KEY,
            purpose="local",
            version=4,
        )
'''
