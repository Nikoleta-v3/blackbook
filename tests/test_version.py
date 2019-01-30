import blackbook


def test_version_is_string():
    assert type(blackbook.__version__) is str
