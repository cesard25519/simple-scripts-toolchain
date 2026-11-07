template_prepared_query: str = """
from typing import Any, Protocol, TypeVar, runtime_checkable
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
