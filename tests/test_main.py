import pathlib

from blackbook.__main__ import main


def test_main_runs_without_failure():
    data_path = pathlib.Path(f"{__file__}").parent / "data" / "formatted"

    assert main(data_path) is None
