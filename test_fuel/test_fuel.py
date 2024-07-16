from fuel import convert, gauge
from pytest import raises


def test_fuel_convert():
    assert convert('99/100') == 99
    assert convert('1/100') == 1
    assert convert('0/100') == 0
    assert convert('100/100') == 100
    assert convert('2/3') == 67


def test_fuel_guage():
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'

def test_fuel_zero():
    with raises(ZeroDivisionError):
        convert('0/0')

def test_fuel_improper():
    with raises(ValueError):
        convert('3/2')


