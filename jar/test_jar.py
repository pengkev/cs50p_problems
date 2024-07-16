from jar import Jar
from pytest import raises

def test_init():
    with raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(10)
    assert str(jar) == "🍪🍪"

def test_deposit():
    jar = Jar()
    with raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    with raises(ValueError):
        jar.withdraw(1)

