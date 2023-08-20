from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar ()
    assert jar.size == 0
    jar.deposit(4)
    assert jar.size == 4

    with pytest.raises(ValueError):
        jar.deposit(100)


def test_withdraw():
    jar = Jar ()
    assert jar.size == 0
    jar.deposit(10)
    assert jar.size == 10
    jar.withdraw(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.withdraw(6)