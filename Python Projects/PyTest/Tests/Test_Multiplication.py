'''
Use the Pytest Paramtrize to assert the multipication within the tuples

'''

# Simple Multipication Scenario
import pytest
products = [
    (2, 4, 8),
    (99, 1, 99),
    (0, 99, 0),
    (5, -4, -20),
    (-9, -9, 81),
    (3.9, 6.7, 26.13)
]

@pytest.mark.parametrize('x, y, result',products)
def Test_multiplication(x, y, result):
    assert x * y == result

def test_one_plus():
    assert 1+1==2

