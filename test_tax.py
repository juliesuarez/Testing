import pytest
from tax import calculate_tax


def test_calculate_tax_below_12000():
    result = calculate_tax(10000)
    assert result == 0.0


def test_calculate_tax_between_12000_and_36000():
    result = calculate_tax(25000)
    assert result == 5000.0


def test_calculate_tax_above_36000():
    result = calculate_tax(40000)
    assert result == 16000.0
