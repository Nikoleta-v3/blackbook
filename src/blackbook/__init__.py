from typing import Iterator, Optional

import re
import pathlib
import json

import black

from .version import __version__


def gen_notebook_files_in_dir(path: pathlib.Path) -> Iterator[pathlib.Path]:

    return path.glob("**/*.ipynb")


def format_notebook_content(path: pathlib.Path) -> Optional[dict]:
    content = path.read_text()
    nb = json.loads(content)

    modification_found = False
    for cell in nb["cells"]:
        try:
            string = "".join(cell["source"])
            formatted_string = black.format_str(
                string, line_length=black.DEFAULT_LINE_LENGTH
            )
            if formatted_string != string:
                modification_found = True
                cell["source"] = [s + "\n" for s in formatted_string.split("\n")][:-1]
        except black.InvalidInput:
            pass

    if modification_found:
        return nb
    return None
