template_config_core: str = """from .settings import Settings


SETTINGS: Settings = Settings()
"""

template_main: str = """from fastapi import FastAPI


from config import SETTINGS

app: FastAPI = FastAPI()


def main() -> None:
    # from api import ...


    # app.include_router(router=_.router)
    ...


if __name__ == '__main__':
    from uvicorn import run

    main()

    run(
        port=SETTINGS.PORT,
        host=SETTINGS.HOST,
        app=app,
    )
"""

template_settings: str = """
from sqlite3 import Connection, connect
from collections.abc import Generator
from contextlib import contextmanager
from functools import cached_property

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


    @property
    @contextmanager
    def Conn(self) -> Generator[Connection, None, None]:
        try:
            with connect(self.DATABASE_URL) as conn:
                yield conn

        finally:
            conn.close()

"""
template_create_tables: str = """from config import SETTINGS


def create_tables() -> None:
    with SETTINGS.Conn as conn:
        with open(file='tables.sql', mode='r') as tables:

            conn.executescript(tables.read())

"""
