from sys import argv as term_args

from utils import (
    __create_dir_and_enter,
    __create_py_file,
    __create_file,
    __move_back,
    __main__,
)

from templates._py_flask_ini import (
    template_flaskenv,
    template_app_ini,
    template_dot_env,
)


def __create_root() -> None:
    # varenv and flaskenv
    __create_file(name='.flaskenv', content=template_flaskenv)
    __create_file(name='.env', content=template_dot_env)


def __create_app() -> None:
    __create_dir_and_enter(name='app')
    __create_py_file(name='__init__', content=template_app_ini)
    __move_back()


def __create_pkg() -> None:
    try:
        app_name: str = term_args[1:].pop()

    except Exception as e: raise ValueError('application name is required')

    __create_dir_and_enter(name=app_name)


@__main__
def main() -> None:
    __create_pkg()
    __create_root()
    __create_app()
