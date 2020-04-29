import pytest
from src.money import Money

def test_exercise():
    a = Money(10,0)
    b = Money(5,0)

    assert str(a.plus(b)) == "15.00p"

    a = Money(10, 0)
    b = Money(3, 0)
    c = Money(5, 0)

    assert not a.less_than(b)
    assert b.less_than(c)

    a = Money(10, 0)
    b = Money(3, 50)

    assert str(a.minus(b)) == "6.50p"
