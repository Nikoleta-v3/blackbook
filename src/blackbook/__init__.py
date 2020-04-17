import json
import pathlib
import re
from typing import Iterator, Optional

import black

from .version import __version__


def gen_notebook_files_in_dir(path: pathlib.Path) -> Iterator[pathlib.Path]:

    return path.glob("**/*.ipynb")


def format_notebook_content(path: pathlib.Path) -> Optional[dict]:
    content = path.read_text()

    try:  # Some ipynb files will not contain json

        nb = json.loads(content)
        modification_found = False

        try:  # Some ipynb files will have no cells

            for cell in nb["cells"]:

                try:  # Some ipynb files will not have valid source code
                    string = "".join(cell["source"])
                    formatted_string = black.format_str(
                        string, mode=black.FileMode()
                    ).strip()  # Remove trailing newlines
                    if formatted_string != string:
                        modification_found = True
                        cell_lines = formatted_string.splitlines()
                        n_last_newline = len(cell_lines) - 1
                        cell["source"] = [
                            line + "\n" if itr < n_last_newline else line
                            for itr, line in enumerate(cell_lines)
                        ]

                except black.InvalidInput:
                    pass

            if modification_found:
                return nb

        except KeyError:
            pass

    except json.JSONDecodeError:
        pass

    return None
