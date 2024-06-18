import pytest
from products import Product

def test_creating_product():
   product1 = Product("MacBook Air M2", 1450, 100)
   assert product1.name == "MacBook Air M2"


def test_product_invalid_price():
   with pytest.raises(ValueError):
      Product("", price=1450, quantity=100)
   with pytest.raises(ValueError):
      Product("MacBook Air M2", price=-1, quantity=100)
   with pytest.raises(ValueError):
      Product("MacBook Air M2", price=1450, quantity=-100)


def product_reaches_0quantity():
   product = Product("MacBook Air M2", price=1450, quantity=0)
   assert not product.is_active()


def poduct_modifies_quantity_returns_right_output():
   product1 = Product("MacBook Air M2", 1450, 100)
   total_price = product1.buy(5)
   assert total_price == 1450 * 5
   assert product1.quantity == 95


def larger_quantity_than_exists():
   product = Product("MacBook Air M2", price=1450, quantity=100)
   with pytest.raises(ValueError):
      product.buy(150)













