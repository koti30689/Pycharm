import pytest
def func(x):
    return x + 1

@pytest.mark.deepak
def test_answer():
    assert func(3) == 10