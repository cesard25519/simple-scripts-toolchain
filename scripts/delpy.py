import os


def __remove_pycache(directories: list[str]) -> None:
    for directory in directories.copy():
        if os.path.isdir(directory) and 'pycache' in directory:
            os.system('rm -r ' + directory)
            directories.remove(directory)
            return


def __recursive_deletion(directories: list[str]) -> None:
    for directory in directories:
        if not os.path.isdir(directory):
            continue

        try:
            os.chdir(directory)
            delpy()

        except Exception as e:
            print(e)

        finally:
            os.chdir('..')


def delpy() -> None:
    directories: list[str] = os.listdir()

    __remove_pycache(directories=directories)

    __recursive_deletion(directories=directories)


if __name__ == '__main__':
    delpy()

