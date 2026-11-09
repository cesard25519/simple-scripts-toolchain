from typing import NamedTuple, Self


class Namespace(NamedTuple):
    settings: str
    mod: str


    @classmethod
    def as_fold(cls) -> Self:
        return cls(
            settings=settings,
            mod=mod,
        )


mod: str = """from .settings import Settings


SETTINGS: Settings = Settings()
"""

settings: str = """from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict

from pyseto import Key, KeyInterface


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_file='.env',
    )

    DATABASE_AUTH_TOKEN: str
    DATABASE_URL: str

    TOKEN_KEY_EXPIRE_TIME: int
    TOKEN_KEY: str

    DEBUG: bool
    PORT: int
    HOST: str


    @cached_property
    def KEY_INTERFACE(self) -> KeyInterface:
        return Key.new(
            key=self.TOKEN_KEY,
            purpose="local",
            version=4,
        )
"""

