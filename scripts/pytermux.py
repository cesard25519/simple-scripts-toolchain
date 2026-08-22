from os import system


data: list[str] = []


while True:
    ctt: str = input('')
    data.append(
        ctt
        .replace('/data/data/com.termux/files', '')
        .replace('Android', 'BSD')
        .replace('android', 'bsd')
    )

    if '.?' in ctt:
        system('clear')
        for line in data:
            print(line)
        break
