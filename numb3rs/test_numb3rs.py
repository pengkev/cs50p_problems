from numb3rs import validate

def test_bignum():
    assert validate('256.256.256.256') == False
    assert validate('255.255.255.256') == False
    assert validate('1000.2.2.56') == False
    assert validate('255.256.255.255') == False
    assert validate('25.25.25.25') == True
    assert validate('255.255.255.255') == True



def test_notformatted():
    assert validate('s') == False
    assert validate('234.1421.421.42') == False
