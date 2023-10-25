import pytest
from src.create_svc import create_calculation


def test_create_calculation():
    calculation = create_calculation(2, 3, 5)
    assert calculation.num1 == 2
    assert calculation.num2 == 3
    assert calculation.result == 5
