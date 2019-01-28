import json
import pathlib

import blackbook


def test_format_notebook_content():
    data_path = pathlib.Path(f"{__file__}").parent / "data"
    source_notebook_path = data_path / "spaces.ipynb"
    output_json = blackbook.format_notebook_content(source_notebook_path)

    formatted_notebook_path = data_path / "formatted_spaces.ipynb"
    expected_content = formatted_notebook_path.read_text()
    expected_json = json.loads(expected_content)
    assert all(
        [
            cell["source"] == expected_cell["source"]
            for cell, expected_cell in zip(output_json["cells"], expected_json["cells"])
        ]
    )


def test_format_notebook_content_does_nothing_with_formatted_notebook():
    data_path = pathlib.Path(f"{__file__}").parent / "data"
    formatted_notebook_path = data_path / "formatted_spaces.ipynb"
    assert blackbook.format_notebook_content(formatted_notebook_path) is None
