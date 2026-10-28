from dataclasses import dataclass, field
from sys import argv as words
import os


@dataclass
class WordFinder:
    words: list[str] = field(default_factory=lambda: words[1:])
    divider: str = 'home'
    trace_dir: str = '/'


    def __call__(self) -> None:
        self.__rcv_finder()


    def __exists_word(self, line: str) -> str:
        for word in self.words:
            if word in line:
                return line.replace(word, f'\033[34m{word}\033[0m')
        return line


    def __find_word(self, filename: str) -> None:
        with open(filename, 'r', errors='ignore', encoding='utf-8') as file:
            for n, line in enumerate(file, 1):
                line = f'\n\033[31m{line}\033[0m'
                fmtd = self.__exists_word(line)

                if len(fmtd) == len(line): continue

                print(
                    f'\033[1;36m{self.__fmt_filename(self.trace_dir + filename)}\033[0m'
                    f'\n{" " * 6}|\n\033[33m{self.__fmt_line_number(n)}\033[0m'
                    f'| \033[31m{fmtd.strip()}\033[0m{" " * 6}|\n'
                )


    def __fmt_filename(self, s: str, c: int = 60) -> str:
        return s[:c - 3] + '...' if len(s) >= c else s + ' ' * (c - len(s))


    def __fmt_line_number(self, i: int) -> str:
        s = str(i)
        return s[:3] + '...' if len(s) >= 5 else s + ' ' * (6 - len(s))


    def __rcv_finder(self) -> None:
        home = os.getcwd().split(self.divider)[1]
        self.trace_dir = home.removeprefix(self.trace_dir) + '/'

        for d in os.listdir():
            if os.path.isfile(d):
                try: self.__find_word(d)

                except Exception as e: print(f'conflict in : {d}: {e}')
                continue

            try:
                os.chdir(d)
                self.__rcv_finder()

            except Exception as e: print(e)

            finally: os.chdir('..')


if __name__ == '__main__':
    WordFinder()()
