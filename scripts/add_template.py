from typing import NamedTuple
from pprint import pprint
from sys import argv

from utils import __main__
from _templates import (
    dot_env_pg,
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
        'dotenv-pg': Code(
            content=dot_env_pg,
            name='.env',
        )
    },
    'py': {
        'sample': Code(
            content='',
            name=''
        ),
    },
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

    print(f'created successfully at `./` with name {code.name}')
