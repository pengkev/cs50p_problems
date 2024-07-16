from seasons import birth_get
from pytest import raises
import datetime

def test_badinput():
    assert birth_get('2000-12-01') == datetime.date(2000,12,1)
    with raises(SystemExit):
        birth_get('2000-13-01')
    with raises(SystemExit):
        birth_get('2000-12-32')



