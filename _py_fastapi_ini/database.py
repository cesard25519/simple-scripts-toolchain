from typing import NamedTuple, Self

class Namespace(NamedTuple):
    prepare: str
    sqlite: str
    mod: str
    pg: str


    @classmethod
    def as_fold(cls) -> Self:
        return cls(
            sqlite=sqlite_prepare,
            prepare=prepare,
            pg=pg_prepare,
            mod=mod,
        )

mod: str = """from .sqlite import PreparedQuery as SqlitePrepare
from .prepare import Void, Pool, ID, Subject
from .pg import PreparedQuery as PgPrepare
"""


prepare: str = """from typing import Any, Protocol, TypeVar,\\
    runtime_checkable, Callable, NamedTuple


T = TypeVar('T')


type Void = Callable[..., None]
Pool: type = Any
ID: type = int


class Subject(NamedTuple):
    id: ID


class CursorInfo(NamedTuple):
    rows: list
    changes: int = 0
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
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Generator


from .prepare import Prepare, CursorInfo
from config import SETTINGS


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
pg_prepare: str = """
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Generator


from psycopg2.extensions import connection as Connection, cursor
from psycopg2.pool import ThreadedConnectionPool

from .prepare import Prepare, CursorInfo
from config import SETTINGS

try:
    _pool: ThreadedConnectionPool = ThreadedConnectionPool(
        dsn=SETTINGS.DATABASE_DSN,
        maxconn=10,
        minconn=1,
    )
except Exception as e:
    print(str(e))


@dataclass
class PreparedQuery(Prepare):
    sql: str


    @contextmanager
    def _connect(self) -> Generator[cursor, None, None]:
        conn: Connection = _pool.getconn()
        try:
            with conn.cursor() as cur:
                yield cur

        except Exception as e:
            conn.rollback()
            raise

        finally:
            _pool.putconn(conn)


    def get(self, *p: Any) -> tuple | None:
        with self._connect() as conn:
            conn.execute(self.sql, tuple(p))
            return conn.fetchone()


    def run(self, *p: Any) -> CursorInfo:
        with self._connect() as conn:
            conn.execute(self.sql, tuple(p))

            return CursorInfo(
                last_row_inserted_id=conn.lastrowid,
                rows=conn.fetchmany(),
                changes=conn.rowcount,
            )


    def all(self, *p: Any) -> list[tuple]:
        with self._connect() as conn:
            conn.execute(self.sql, tuple(p))
            return conn.fetchall()


    def exec(self) -> None:
        with self._connect() as conn:
            conn.execute(self.sql)

"""

