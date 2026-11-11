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


from config import SETTINGS
from api import router


app: FastAPI = FastAPI()
app.include_router(router=router())


if __name__ == '__main__':
    run(
        port=SETTINGS.PORT,
        host=SETTINGS.HOST,
        app=app,
    )
"""


