from um import count
import pytest

def test_none():
    assert count("none at all") == 0
    assert count("klusums") == 0

def test_some():
    assert count("um, what's up?") == 1
    assert count("um, um, um") == 3
    assert count("IS THIS UM LOUD ENOUGH?") == 1


def text_edgecases():
    with pytest.raises(ValueError):
            count(7)
