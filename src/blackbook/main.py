""""""

from typing import Iterator

import re
import pathlib

import black


JUPYTER_REGEX = re.compile(r"\.ipynbi?$")


def gen_notebook_files_in_dir(
        path: pathlib.Path,
) -> Iterator[pathlib.Path]:

    return path.glob("**/*.ipynb")
