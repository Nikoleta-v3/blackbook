import json
import pathlib

import blackbook


def test_format_notebook_content():
    data_path = pathlib.Path(f'{__file__}/data/')
    source_notebook_path = data_path / 'spaces.ipynb'
    output_json = blackbook.format_notebook_content(source_notebook_path)

    formatted_notebook_path = data_path / 'formatted_spaces.ipynb'
    expected_json = json.load(formatted_notebook_path)

    assert output_json == expected_json