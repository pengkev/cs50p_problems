import project

def test_rate_rarity():
    test = project.rate_rarity('Kevin')
    assert test > 0 & test < 25
    assert type(test) == type(int())

def test_rate_value():
    test = project.rate_value('Kevin')
    assert test > 0 & test < 25
    assert type(test) == type(int())

def test_rate_nicknames():
    test = project.rate_nicknames('Kevin')
    assert test > 0 & test < 25
    assert type(test) == type(int())

def test_rate_pronounceability():
    test = project.rate_pronounceability('Kevin')
    assert test > 0 & test < 25
    assert type(test) == type(int())
