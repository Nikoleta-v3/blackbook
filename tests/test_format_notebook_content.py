import json
import pathlib
import shutil

import blackbook


def test_format_notebook_content():
    data_path = pathlib.Path(f"{__file__}").parent / "data"
    source_notebook_path = data_path / "unformatted" / "spaces.ipynb"
    output_json = blackbook.format_notebook_content(source_notebook_path)

    formatted_notebook_path = data_path / "formatted" / "spaces.ipynb"
    expected_content = formatted_notebook_path.read_text()
    expected_json = json.loads(expected_content)
    assert all(
        [
            cell["source"] == expected_cell["source"]
            for cell, expected_cell in zip(output_json["cells"], expected_json["cells"])
        ]
    )


def test_format_single_notebook():
    """
    Test formatting a single notebook in an directory of unformatted notebooks
    formats only that notebook
    """
    data_path = pathlib.Path(f"{__file__}").parent / "data"
    source_notebook_path = data_path / "unformatted" / "spaces.ipynb"
    copy_notebook_path = data_path / "unformatted" / "spaces_copy.ipynb"
    shutil.copy(str(source_notebook_path), str(copy_notebook_path))

    source_json = json.loads(source_notebook_path.read_text())
    copy_json = json.loads(copy_notebook_path.read_text())

    assert all(
        [
            copy_cell["source"] == source_cell["source"]
            for copy_cell, source_cell in zip(copy_json["cells"], source_json["cells"])
        ]
    )

    # Have to run blackbook main to show spaces_copy.ipynb is unaffected
    blackbook.__main__.main(source_notebook_path)
    output_json = json.loads(source_notebook_path.read_text())
    check_copy_json = json.loads(copy_notebook_path.read_text())
    shutil.copy(str(copy_notebook_path), str(source_notebook_path))
    pathlib.Path.unlink(copy_notebook_path)

    assert not all(
        [
            formatted_cell["source"] == unformatted_cell["source"]
            for formatted_cell, unformatted_cell in zip(
                output_json["cells"], check_copy_json["cells"]
            )
        ]
    )


def test_format_notebook_content_does_nothing_with_formatted_notebook():
    data_path = pathlib.Path(f"{__file__}").parent / "data"
    formatted_notebook_path = data_path / "formatted" / "spaces.ipynb"
    assert blackbook.format_notebook_content(formatted_notebook_path) is None
