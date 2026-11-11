from typing import NamedTuple, Self


class Namespace(NamedTuple):
    err: str
    mod: str


    @classmethod
    def as_fold(cls) -> Self:
        return cls(
            err=err,
            mod=mod,
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
mod: str = """from fastapi import APIRouter


from . import *


_paths: list = [] # modules


def router() -> APIRouter:
    app: APIRouter = APIRouter(
        prefix='/api/v1',
        tags=['v1'],
    )

    for path in _paths:
        app.include_router(router=path.router)

    return app
"""

