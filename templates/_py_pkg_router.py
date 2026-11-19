init_router: str = """from fastapi import APIRouter


from .repository import Repository


router: APIRouter = APIRouter(prefix='/__name__', tags=['__name__'])


repo: Repository = Repository(); repo.create_table()
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

repository: str = '''from config.database import SqlitePrepare as Prepare, Void


class Repository:
    create_table: Void = Prepare("""
    --.======================================================================
    --.                             turso scheme
    --.======================================================================
    CREATE TABLE IF NOT EXISTS __name__(
        created_at date NOT NULL DEFAULT CURRENT_TIMESTAMP,
        id uuid PRIMARY KEY DEFAULT uuid4(),

        --...
    ) STRICT;
    """).exec

'''
