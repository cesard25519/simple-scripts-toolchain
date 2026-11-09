from sys import argv as term_args


from _utils import (
    __create_dir_and_enter,
    __create_py_file,
    __move_back,
)


def __create_pkg() -> None:
    try:
        app_name: str = term_args[1:].pop()

    except Exception as e:
        raise ValueError('application name is required ' +  str(e))

    __create_dir_and_enter(name=app_name)



def create_files_from_namespace(n: dict[str, str]) -> None:
    for name, template in n.items():
        if name == 'mod': name = '__init__'

        if name.startswith('dot'):
            name = '.' + name.removeprefix('dot_')

        __create_py_file(name=name, content=template)


def create_files_from_namespace_and_exit(n: dict) -> None:
    create_files_from_namespace(n=n)
    __move_back()
