template_dot_gitignore: str = """.env
"""

template_main: str = """from dotenv import load_dotenv


from app import (
    Application,
    __run_serve,
    create_app,
)


load_dotenv()


api: Application = Application()
api.root_path = '/api'


def main() -> None:
    create_app(app=api)

    __run_serve(app=api)


if __name__ == '__main__':
    main()
"""

template_config: str = """from os import environ as varenv


def __get_varenv(name: str) -> str:
    if var := varenv.get(name):
        return var

    raise NotImplementedError('any varenv doesnt exists or not implemented')
"""


template_app: str = """from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI as Application
from uvicorn import run


from config import __get_varenv # type: ignore
# from api.__ import ___ as Router


def __run_serve(app: Application) -> None:
    return run(
        host=__get_varenv(name='HOST'),
        port=int(__get_varenv(name='PORT')),
        app=app,
    )


def create_app(app: Application) -> None:
    # app.include_router(router=Router)

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
    )
"""
