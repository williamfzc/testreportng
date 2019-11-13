from testreportng.utils import get_timestamp


def test_get_timestamp():
    assert get_timestamp()
    assert get_timestamp(human=True)
