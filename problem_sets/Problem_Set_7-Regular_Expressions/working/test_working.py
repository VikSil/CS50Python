from working import convert
import pytest

def test_standard():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_exceptions():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:99 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 14:00 AM")
    with pytest.raises(ValueError):
        convert("13:00 PM 14:00 AM")



def text_edgecases():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert(12)
