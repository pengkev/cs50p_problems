from bank import value

def test_bank_hello():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('Hello, Mark') == 0

def test_bank_h():
    assert value('hm') == 20
    assert value('Hmph! I hate to see you again Mark') == 20

def test_bank_():
    assert value('Asnjaskn') == 100
    assert value('') == 100
    assert value('12') == 100


