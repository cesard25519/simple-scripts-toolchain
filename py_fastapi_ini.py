from sys import argv as term_args

from utils import (
    __create_dir_and_enter,
    __create_py_file,
    __create_dotenv,
    __create_dir,
    __move_back,
    __main__,
)

from templates._py_fastapi_ini import (
    template_config_core,
    template_settings,
    template_main,
)
from templates._py_repository import template_prepared_query


def __create_root() -> None:
    __create_py_file(name='main', content=template_main)
    __create_dotenv()


def __create_pkg() -> None:
    try:
        app_name: str = term_args[1:].pop()

    except Exception as e:
        raise ValueError('application name is required', e)

    __create_dir_and_enter(name=app_name)


def __create_config_pkg() -> None:
    __create_dir_and_enter(name='config')
    __create_py_file(name='__init__', content=template_config_core)
    __create_py_file(name='settings', content=template_settings)

    __create_dir_and_enter(name='database')
    __create_py_file(name='mod', content=template_prepared_query)
    __move_back()

    __create_dir_and_enter(name='security')
    __create_py_file(name='__init__', content='')

    __move_back(); __move_back()


def __create_fold_struct() -> None:
    __create_config_pkg()
    __create_dir(path='core')
    __create_dir(path='api')
    __create_dir(path='model')


@__main__
def main() -> None:
    __create_pkg()

    __create_root()

    __create_fold_struct()


