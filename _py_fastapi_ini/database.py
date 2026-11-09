from typing import NamedTuple, Self


class Namespace(NamedTuple):
    prepare: str
    sqlite: str


    @classmethod
    def as_fold(cls) -> Self:
        return cls(
            sqlite=sqlite_prepare,
            prepare=prepare,
        )



prepare: str = """from typing import Any, Protocol, TypeVar, runtime_checkable
from dataclasses import dataclass, field

T = TypeVar('T')

Pool = Any


@dataclass
class CursorInfo:
    changes: int = 0
    rows: list = field(default_factory=list)
    last_row_inserted_id: int | None = None


@runtime_checkable
class Prepare(Protocol[T]):
    def _connect(self) -> Pool: ...

    def get(self, *p: Any) -> T | None: ...
    def run(self, *p: Any) -> CursorInfo: ...
    def all(self, *p: Any) -> list[T]: ...
    def exec(self) -> None: ...

"""

sqlite_prepare: str = """from sqlite3 import Connection, connect, Cursor
from typing import Any, Generator, Callable
from contextlib import contextmanager
from dataclasses import dataclass


from .prepare import Prepare, CursorInfo
from config import SETTINGS


type Void = Callable[..., None]


@dataclass
class PreparedQuery[T](Prepare[T]):
    sql: str


    @contextmanager
    def _connect(self) -> Generator[Connection, None, None]:
        try:
            with connect(SETTINGS.DATABASE_URL) as conn:
                yield conn

        finally:
            conn.close()


    def get(self, *p: Any) -> T | None:
        with self._connect() as conn:
            return conn.execute(self.sql, tuple(p)).fetchone()


    def run(self, *p: Any) -> CursorInfo:
        with self._connect() as conn:
            res: Cursor = conn.execute(self.sql, tuple(p))
            return CursorInfo(
                last_row_inserted_id=res.lastrowid,
                rows=res.fetchmany(),
                changes=res.rowcount,
            )


    def all(self, *p: Any) -> list[T]:
        with self._connect() as conn:
            return conn.execute(self.sql, tuple(p)).fetchall()


    def exec(self) -> None:
        with self._connect() as conn:
            conn.execute(self.sql)
"""
