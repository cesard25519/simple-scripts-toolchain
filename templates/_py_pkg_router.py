init_router: str = """from fastapi import APIRouter


router: APIRouter = APIRouter(prefix='/__name__', tags=['__name__'])
"""

errors: str = """from fastapi import HTTPException, status


class Error(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='...',
        )
"""

model: str = """from pydantic import BaseModel


class S(BaseModel): ...
"""
