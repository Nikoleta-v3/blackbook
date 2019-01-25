import json
import pathlib
import sys

import blackbook


def main(path=None):
    if path is None:
        path = pathlib.Path(sys.argv[1])

    for notebook_path in blackbook.gen_notebook_files_in_dir(path):
        nb = blackbook.format_notebook_content(notebook_path)

        notebook_path.write_text(json.dumps(nb))

if __name__ == '__main__':
    main()
