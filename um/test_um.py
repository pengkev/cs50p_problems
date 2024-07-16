from um import count

def test_yummy():
    assert count('yummy') == 0
    assert count('sadkl um skdalj') == 1

def test_um():
    assert count('um, hi, um') == 2
    assert count('um?') == 1
    assert count('UM, thanks for the album') == 1
    assert count('Um, hi, uM') == 2


