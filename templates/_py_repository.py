template_prepared_query: str = """
from typing import Any, Callable, Protocol
from dataclasses import dataclass


Pool = Any
Row = tuple


@dataclass
class Result:
    changes: int = 0
    rows: list = []
    last_row_inserted_id: int | None = None


Get = Callable[..., Row | None]
Run = Callable[..., Result]
Exec = Callable[..., None]
All = Callable[..., list]


POOL: Pool = Pool


class Prepare(Protocol):
    cur: Callable[..., Pool]

    def get(self, *p: Any) -> Row | None: ...

    def run(self, *p: Any) -> Result: ...

    def all(self, *p: Any) -> list: ...

    def exec(self) -> None: ...

"""
