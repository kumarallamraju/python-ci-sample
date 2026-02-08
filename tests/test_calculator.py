import pytest
from app.calculator import add, subtract, divide

def test_add(): assert add(2,3)==5

def test_subtract(): assert subtract(10,7)==3

def test_divide(): assert divide(10,2)==5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError): divide(1,0)
