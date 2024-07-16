from plates import is_valid

def test_plates_length():
    assert is_valid('A') == False
    assert is_valid('aaaaaaa') == False
    assert is_valid('aaAaa') == True

def test_plates_f2alpha():
    assert is_valid('h2') == False
    assert is_valid('2d') == False
    assert is_valid('2svg') == False
    assert is_valid('21svg') == False
    assert is_valid('hither') == True
    assert is_valid('ui') == True

def test_plates_numend():
    assert is_valid('MAR1O') == False
    assert is_valid('Wowbr0') == False
    assert is_valid('MR100') == True

def test_plates_spp():
    assert is_valid('MR 100') == False
    assert is_valid('HI!!!!') == False
    assert is_valid('HI.') == False
    assert is_valid('lebron') == True

