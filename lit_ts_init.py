from typing import Callable


from templates._ts_ini_templates import counter_model, counter_component, counter_style
from utils import (
    __create_dir_and_enter,
    __create_file_and_exit,
    __move_back,
    __main__,
    __exec,
)


def _create_fold_structure() -> None:
    __create_dir_and_enter(name='src')

    # src/components
    __create_dir_and_enter(name='components')
    __create_file_and_exit(
        content=counter_component,
        name='xCounter.ts',
    )

    # src/models
    __create_dir_and_enter(name='models')
    __create_file_and_exit(
        content=counter_model,
        name='counter.ts',
    )

    # src/styles
    __create_dir_and_enter(name='styles')
    __create_file_and_exit(
        content=counter_style,
        name='counter.css',
    )

    __move_back()


def _create_main_ts() -> None:
    template: list[str] = [
        "import './src/components/xCounter';",
        "import { XCounter } from './src/components/xCounter';",
        '',
        '',
        'declare global {',
        '    interface HTMLElementTagNameMap {',
        "        'x-counter': XCounter;",
        '    }',
        '}',
    ]
    with open('main.ts', 'w') as main_ts:
        main_ts.writelines(t + '\n' for t in template)


def _fmt_index_html() -> None:
    old_doc: list[str] = []

    double_space: str = '  '

    with open('index.html', 'r') as index:
        for line in index.readlines():
            striped_starts: Callable = line.strip().startswith

            if striped_starts('<link'):
                line = line.replace('./src/', '')

            if striped_starts('<script'):
                line = line.replace('src/my-element', 'main')

            if striped_starts('<my-element'):
                line = line.replace('my-element', 'x-counter></x-counter')

            if striped_starts('</my-element') or striped_starts('<h1'):
                continue

            old_doc.append(
                line.replace(
                    double_space,
                    double_space*2
                )
            )

    with open('index.html', 'w') as index:
        index.writelines(old_doc)


def _alloc_index_in_root() -> None:
    __exec('mv src/index.css .')

    lines: list[str] = []
    with open('index.css', 'r') as css:
        for line in css:
            lines.append(line.replace('  ', '    '))

    with open('index.css', 'w') as css:
        css.writelines(lines)


def _clean_src() -> None:
    __exec('rm -r src')



@__main__
def main() -> None:
    _alloc_index_in_root()
    _clean_src()
    _create_fold_structure()
    _create_main_ts()
    _fmt_index_html()
