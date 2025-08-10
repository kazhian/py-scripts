import pytest

def add (a,b):
    return a + b

def div(a,b):
    return a/b

def test_add():
    assert add(1,1) ==2

def test_div():
    assert div(1,1) == 1

# Testing Exceptions
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1,0)