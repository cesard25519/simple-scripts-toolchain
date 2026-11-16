template_prepared_query: str = """from typing import Any, Protocol, TypeVar,\\
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


