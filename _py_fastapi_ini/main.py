from _util import create_files_from_namespace_and_exit,\
    create_files_from_namespace, __create_pkg

from _utils import __create_dir_and_enter, __move_back, __create_dir, __main__

from database import Namespace as Database
from security import Namespace as Security
from config import Namespace as Config
from root import Namespace as Root
from api import Namespace as Api


@__main__
def main() -> None:
    # ?/
    __create_pkg()
    create_files_from_namespace(n=Root.as_fold()._asdict())

    # ?/config
    __create_dir_and_enter(name='config')
    create_files_from_namespace(n=Config.as_fold()._asdict())


    # ?/config/database
    __create_dir_and_enter(name='database')
    create_files_from_namespace_and_exit(n=Database.as_fold()._asdict())


    # ?/config/security
    __create_dir_and_enter(name='security')
    create_files_from_namespace_and_exit(n=Security.as_fold()._asdict())

    # ?/
    __move_back()

    # ?/
    __create_dir_and_enter(name='api')
    create_files_from_namespace_and_exit(n=Api.as_fold()._asdict())

    __create_dir('tools')




