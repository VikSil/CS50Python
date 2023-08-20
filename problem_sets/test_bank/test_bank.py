from bank import value


def test_hundread():
    assert value("cat") == 100
    assert value("value") == 100

def test_zero():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_twenty():
    assert value("Howdy") == 20
    assert value("Holy Hell") == 20

""""
def test_number():
    with pytest.raises(AttributeError):
        value(2)
"""