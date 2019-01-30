import pathlib

import blackbook


def test_gen_notebook_files_in_dir():
    path = pathlib.Path(".").resolve()

    nbs = blackbook.gen_notebook_files_in_dir(path)
    expected_nbs_names = sorted(
        [("unformatted", "spaces.ipynb"), ("formatted", "spaces.ipynb")]
    )
    assert (
        sorted([nb.parts[-2:] for nb in nbs if "checkpoint" not in str(nb)])
        == expected_nbs_names
    )
