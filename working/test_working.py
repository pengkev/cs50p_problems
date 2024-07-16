from working import convert
from pytest import raises

def test_convertAMPM():
    assert convert('9 AM to 8 PM') == '09:00 to 20:00'
    assert convert('1 AM to 2 PM') == '01:00 to 14:00'

def test_convertPMAM():
    assert convert('9 PM to 8 AM') == '21:00 to 08:00'
    assert convert('2 PM to 6 AM') == '14:00 to 06:00'

def test_convertmidnightnoon():
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'
    assert convert('12 PM to 12 AM') == '12:00 to 00:00'

def test_colon():
    assert convert('12:00 AM to 12:01 PM') == '00:00 to 12:01'
    assert convert('9:57 PM to 1:21 PM') == '21:57 to 13:21'

def test_noto():
    with raises(ValueError):
        convert('sakdnasldn')
    with raises(ValueError):
        convert('9 AM 9 PM')

def test_range():
    with raises(ValueError):
        convert('13 AM to 1 PM')
    with raises(ValueError):
        convert('12:60 PM to 1:60 PM')
    with raises(ValueError):
        convert('1 PM to 13 AM')
    with raises(ValueError):
        convert('13:01 AM to 1:61 AM')
