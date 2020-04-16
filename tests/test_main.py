import pathlib

import pytest

from blackbook.__main__ import main


def test_main_runs_without_failure():
    data_path = pathlib.Path(f"{__file__}").parent / "data" / "formatted"

    assert main(data_path) is None


def test_invalid_path():
    with pytest.raises(OSError):
        data_path = pathlib.Path(f"{__file__}").parent / "invalid"
        main(data_path)
