from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/1") == 0

def test_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("4/2")
    with pytest.raises(ValueError):
        convert("cat")


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(33) == "33%"