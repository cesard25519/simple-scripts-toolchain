from os import system


class PyTermux:
    def __init__(self) -> None:
        self._data: list[str] = []
        self._ctt: str = ''


    def __call__(self) -> None:
        while True:
            self._ctt = input('')

            if self.__eval_end_mark():
                return

            if self.__replace_all():
                continue

            self.__save_line()


    def __replace_all(self) -> bool:
        is_replaceable: bool = self._ctt.startswith('::')

        if is_replaceable:
            to_replace, new = self._ctt[2:].split('.')
            print(to_replace, new)

            self._data = [
                line
                .replace(to_replace, new)
                for line in self._data
            ]

        return is_replaceable


    def __save_line(self) -> None:
        self._data.append(
            self._ctt
            .replace('/data/data/com.termux/files', '')
            .replace('Android', 'BSD')
            .replace('android', 'bsd')
        )


    def __eval_end_mark(self) -> bool:
        is_mark: bool = '?' in self._ctt

        if is_mark:
            system('clear')
            for line in self._data:
                print(line)

        return is_mark


if __name__ == '__main__':
    term: PyTermux = PyTermux()
    term()
