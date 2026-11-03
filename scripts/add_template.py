from typing import NamedTuple
from pprint import pprint
from sys import argv

from utils import __main__
from _templates import (
    dotenv_pg, dotenv,
    blank_py,
)

temp_names: list[str] = argv[1:]

class Command(NamedTuple):
    lang: str
    template: str


class Code(NamedTuple):
    content: str
    name: str


langs: dict[str, dict[str, Code]] = {
    '_': {
        'dotenv-pg': Code( content=dotenv_pg, name='.env' ),
        'dotenv': Code( content=dotenv, name='.env' ),
    },
    'py': {
        '_': Code( content=blank_py, name='main.py' ),
    }
}

@__main__
def main() -> None:
    if not temp_names or temp_names[0] in ( '-h', '--h', '--help' ):
        return pprint('Uses `<CMD> <lang> <template_name>`')

    cmd: Command = Command(*temp_names)

    if not ( template := langs.get(cmd.lang) ):
        return pprint('lang not found')

    if not ( code := template.get(cmd.template) ):
        return pprint('snippet not found')

    with open(code.name, 'w', encoding='utf-8') as writer:
        writer.write(code.content)

    print(f'created successfully with name {code.name} in this directory')
