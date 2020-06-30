import pytest


@pytest.mark.xfail(reason="Buggy banana")
def test_banana():
    assert False
