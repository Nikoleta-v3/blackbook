import json
import pathlib
import sys

from loguru import logger

import blackbook


def main(path: pathlib.Path = None) -> None:
    if path is None:  # pragma: no cover
        path = pathlib.Path(sys.argv[1])
    if not path.exists():
        raise OSError(f"The path {path} is invalid.")

    count = 0
    reformatted_count = 0

    notebooks = (
        [path] if path.suffix == ".ipynb" else blackbook.gen_notebook_files_in_dir(path)
    )
    for notebook_path in notebooks:
        nb = blackbook.format_notebook_content(notebook_path)

        if nb is not None:  # pragma: no cover
            notebook_path.write_text(json.dumps(nb))
            reformatted_count += 1

        count += 1

    logger.info(f"All done! 📖")
    logger.info(
        f"{reformatted_count} notebooks reformatted. {count - reformatted_count} left unchanged."
    )


if __name__ == "__main__":  # pragma: no cover
    main()
