# test_math_functions.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def test_addition():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0

def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(10, 7) == 3

# This function will not be considered as a test case by pytest
def helper_function():
    pass
