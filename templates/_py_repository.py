template_prepared_query: str = """
from typing import Any, Callable, Protocol
from dataclasses import dataclass


Pool = Any


@dataclass
class Result:
    changes: int = 0
    rows: list = []
    last_row_inserted_id: int | None = None


Get = Callable[..., tuple[Any] | None]
Run = Callable[..., Result]
Exec = Callable[..., None]
All = Callable[..., list]


POOL: Pool = Pool


class Prepare(Protocol):
    def _connect(self) -> Pool: ...

    def get(self, *p: Any) -> tuple[Any]| None: ...

    def run(self, *p: Any) -> Result: ...

    def all(self, *p: Any) -> list[Any]: ...

    def exec(self) -> None: ...

"""

