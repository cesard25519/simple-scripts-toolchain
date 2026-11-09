from typing import NamedTuple, Self


class Namespace(NamedTuple):
    err: str


    @classmethod
    def as_fold(cls) -> Self:
        return cls(
            err=err,
        )


err: str = """from fastapi import HTTPException, status


class InternalServerError(HTTPException):
    def __init__(self) -> None:
        super().__init__( status_code=status.HTTP_500_INTERNAL_SERVER_ERROR )


class NotFound(HTTPException):
    def __init__(self, e: str) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{ e } not found'
        )


"""

