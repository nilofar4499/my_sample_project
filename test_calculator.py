from calculator import add, subtract, multiply, even


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(2, 3) == 6


def test_even():
    assert even(4) == "even"


def test_odd():
    assert even(7) == "odd"