from numb3rs import validate
import pytest

def test_legit():
    assert validate("1.1.1.1") == True
    assert validate("127.0.0.1") == True


def test_wrong():
    assert validate("Something") == False
    assert validate("427.0.0.1") == False
    assert validate("127.0.0.1.") == False
    assert validate("127.444.444.444") == False