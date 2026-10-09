from sys import argv as words
import os


class WordFinder:
    def __init__(self) -> None:
        self._words: list[str] = words[1:]
        self._divider: str = 'home'
        self._trace_dir: str = '/'


    def __call__(self) -> None:
        self.__rcv_finder()


    def __exists_word(self, line: str) -> str:
        for word in self._words:
            if word in line:
                return line.replace(word, f'\033[34m{ word }\033[0m')

        return line


    def __find_word(self, filename: str) -> None:
        with open(filename, 'r', errors='ignore', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line: str = f'\n\033[31m{ line }\033[0m'

                fmtd_word: str = self.__exists_word(line=line)

                if len(fmtd_word) == len(line): continue

                print(
                    f'\033[1;36m{ self.__fmt_filename(s=self._trace_dir +  filename)}\033[0m'
                    f'\n{ " " * 6 }|\n'
                    f'\033[33m{ self.__fmt_line_number(i=line_number) }\033[0m'
                    f'| \033[31m{ fmtd_word.strip() }\033[0m'
                    f'{ " " * 6 }|\n'
                )


    def __fmt_filename(self, s: str) -> str:
        large: int = len(s)
        constant: int = 40
        return s[:constant - 3] + '...' if large >= constant else s + ' ' * (constant - large)


    def __fmt_line_number(self, i: int) -> str:
        large: int = len(str(i))
        return str(i)[:3] + '...' if large >= 5 else str(i) + ' ' * (6 - large)


    def __rcv_finder(self) -> None:
        directories: list[str] = os.listdir()

        home: str = os.getcwd().split('home')[1]
        self._trace_dir = home.removeprefix(self._trace_dir) + '/'

        for directory in directories:
            if not os.path.isdir(directory) and os.path.isfile(directory):
                try:
                    self.__find_word(filename=directory)

                except Exception as e: print(f'conflict in : { directory }: { e }')
                continue

            try:
                os.chdir(directory)
                self.__rcv_finder()

            except Exception as e: print(e)

            finally: os.chdir('..')





if __name__ == '__main__':
    finder: WordFinder = WordFinder()

    finder()
