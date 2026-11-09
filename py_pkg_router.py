from sys import argv as term_args


from templates._py_pkg_router import (
    init_router,
    repository,
    errors,
)
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

        __create_py_file(name='err', content=errors)

        __create_py_file(
            content=repository.replace('__name__', router_name),
            name='repository',
        )

        __create_file_and_exit(
            content=init_router.replace('__name__', router_name),
            name='__init__.py',
        )


