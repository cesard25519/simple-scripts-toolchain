from sys import argv
from os import scandir


argv.pop(0)


def countlines(route: str, total: int = 0) -> int:
    for entry in scandir(route):
        if entry.name in argv:
            continue

        print('scaning: ' + entry.name)

        if entry.is_file():
            with open(entry.path, encoding='utf-8', errors='ignore') as f:
                total += sum(1 for _ in f)

        if entry.is_dir():
            total += countlines(entry.path)


    return total


if __name__ == '__main__':
    print('Total lines: ', countlines('.'))
