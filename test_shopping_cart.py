"""
Each function that passes is a unit test that passes.
Each function test must have the word test.
Even files to be tested must have the word test.
In python we use a key word 'assert' to check if the statement is true.
If it's not, an error message will appear and you can see where your code failed in testing.
if you need to test a particular function ie
pytest test_shopping_cart.py::then function name
pytest test_shopping_cart.py::test_can_get_total_price -s, 
'-s' forces print statements to show up in the terminal.
"""

from shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add('apple')
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    cart.add('apple')
    assert 'apple' in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    with pytest.raises(OverflowError): #Use the raises helper to assert that some code raises an exception:
        for i in range(6):
            cart.add('apple')


def test_can_get_total_price(cart):
    cart.add('apple')
    cart.add('orange')

    price_map = {'apple': 1.0,'orange': 2.0 }
    assert cart.get_total_price(price_map) == 3.0
    #print('Testing can get price')
  