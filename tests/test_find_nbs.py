def test_find_nbs():
    nbs = blackbook.find_nbs(".")
    expected_nbs_names = sorted(["spaces.ipynb"])
    assert sorted([nb.stem for nb in nbs]) == expected_nbs_names
