from os import (
    mkdir as __create_dir,
    chdir as __move_to,
    system as __exec,
)


from typing import Callable


__move_back: Callable[[], None] = lambda: __move_to('..')
__main__: Callable = lambda _: _()


def __create_dir_and_enter(name: str) -> None:
    __create_dir(name)
    __move_to(name)


def __create_file(name: str, content: str) -> None:
    with open(name, 'w') as doc:
        doc.write(content)


def __create_py_file(name: str, content: str) -> None:
    return __create_file(name=name + '.py', content=content)


def __create_file_and_exit(name: str, content: str) -> None:
    __create_file(name=name, content=content)
    __move_back()


