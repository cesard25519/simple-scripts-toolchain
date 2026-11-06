from sys import argv as term_args


from templates._py_pkg_router import init_router, errors
from utils import (
    __create_dir_and_enter,
    __create_file_and_exit,
    __create_py_file,
    __main__,
)


@__main__
def main() -> None:
    for router_name in term_args[1:]:
        __create_dir_and_enter(name=router_name)

        ctt: str = init_router.replace('__name__', router_name)

        __create_py_file(name='repository', content='')
        __create_py_file(name='err', content=errors)

        __create_file_and_exit(name='__init__.py', content=ctt)
