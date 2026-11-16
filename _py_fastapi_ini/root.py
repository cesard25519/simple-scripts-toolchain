from typing import NamedTuple, Self


class Namespace(NamedTuple):
    main: str
    dot_gitignore: str


    @classmethod
    def as_fold(cls) -> Self:
        return cls(
            dot_gitignore=dot_gitignore,
            main=main,
        )


dot_gitignore: str = """
__pycache__/
.env
.gitignore
"""


main: str = """from fastapi import FastAPI
from uvicorn import run


from api import create_router
from config import SETTINGS


app: FastAPI = FastAPI()
create_router(app=app)


if __name__ == '__main__':
    run(
        port=SETTINGS.PORT,
        host=SETTINGS.HOST,
        reload=True,
        app=app,
    )
"""


