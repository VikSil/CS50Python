from plates import is_valid


def test_wrongstart():
    assert is_valid("99cats") == False
    assert is_valid("1more") == False
    assert is_valid("**ME**") == False
    assert is_valid("44") == False
    assert is_valid("4U") == False

def test_tooshort():
    assert is_valid("I") == False
    assert is_valid("U") == False

def test_toolong():
    assert is_valid("Increadiblylongnumberplate") == False
    assert is_valid("IWillNotStopRocking") == False

def test_midlenumbers():
    assert is_valid("II33II") == False
    assert is_valid("IL0v3U") == False

def test_punctuation():
    assert is_valid("Love U") == False
    assert is_valid("It'sMe") == False

def test_zerofirst():
    assert is_valid("ABBA02") == False
    assert is_valid("ABC01") == False

def test_valid():
    assert is_valid("II4567") == True
    assert is_valid("ALLIT") == True

""""
def test_number():
    with pytest.raises(AttributeError):
        is_valid(2)
"""