from utils import (
    __create_dir_and_enter,
    __create_py_file,
    __create_dotenv,
    __create_file,
    __create_dir,
    __move_back,
    __main__,
)

from templates._py_tools import (
    template_regex_builder,
    template_hash_argon2id,
    template_date_unix,
    template_date_iso,
)

from templates._py_backend import (
    template_dot_gitignore,
    template_config,
    template_main,
    template_app,
)


def __create_root() -> None:
    # varenv and gitignore
    __create_file(name='.gitignore', content=template_dot_gitignore)
    __create_dotenv()

    # base code
    __create_py_file(name='config', content=template_config)
    __create_py_file(name='main', content=template_main)
    __create_py_file(name='app', content=template_app)


def __create_all_dirs() -> None:
    __create_dir('database')
    __create_dir('model')
    __create_dir('core')

    create_tools()


def create_tools() -> None:
    __create_dir_and_enter(name='tools')
    __create_regex_tool_()
    __create_hash_tool_()
    __create_date_tool_()


def __create_regex_tool_() -> None:
    __create_dir_and_enter(name='regex')
    __create_py_file(name='builder', content=template_regex_builder)
    __move_back()

def __create_hash_tool_() -> None:
    __create_dir_and_enter(name='hashing')
    __create_py_file(name='argon2id', content=template_hash_argon2id)
    __move_back()


def __create_date_tool_() -> None:
    __create_dir_and_enter(name='date')
    __create_py_file(name='unix', content=template_date_unix)
    __create_py_file(name='iso', content=template_date_iso)
    __move_back()


@__main__
def main() -> None:
    __create_root()
    __create_all_dirs()


