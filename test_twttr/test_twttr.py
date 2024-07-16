from twttr import shorten
from pytest import raises

def test_twttr_str():
    assert shorten('what\'s good brOski?') == 'wht\'s gd brsk?'
    assert shorten('123123') == '123123'
    assert shorten('aeiou') == ''

def test_twttr_int():
    with raises(TypeError):
        shorten(0)

