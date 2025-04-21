import pytest
from store_2 import Store
from product_2_step_2 import *


def test_add_product():
    store = Store()
    product = Product("Test Product", price=100.0, quantity=20)

    store.add_product(product)

    assert product in store.products
    assert len(store.products) == 1

def test_add_invalid_product():
    store = Store()

    with pytest.raises(TypeError, match="Only instances of Product can be added."):
        store.add_product("not a product")

def test_buy_valid_quantity():
    product = Product("PhoneX", price=100, quantity=4)

    total_cost = product.buy(3)

    assert total_cost == 300
    assert product.quantity == 1

def test_buy_too_much():
    product = Product("PhoneX", price=100, quantity=4)

    with pytest.raises(ValueError, match="Not enough stock to complete purchase."):
        product.buy(5)

    assert product.quantity == 4

def test_product_deactivates_when_zero_quantity():
    product = Product("Laptop", price=1000, quantity=2)

    product.buy(1)
    assert product.quantity == 1
    assert product.is_active() is True

    product.buy(1)
    assert product.quantity == 0
    assert product.is_active() is False

def test_non_stocked_product():
    non_stocked_prod = NonStockedProduct("Windows License", price=125, promotion=None)

    total_cost = non_stocked_prod.buy(3)
    assert total_cost == 375
    assert non_stocked_prod.quantity is None

    non_stocked_prod.buy(3)
    assert non_stocked_prod.is_active() is True

def test_non_stocked_prod_order():
    store = Store()
    non_stocked_prod = NonStockedProduct("Windows License", price=125, promotion=None)

    store.add_product(non_stocked_prod)

    shopping_list = [(non_stocked_prod, 5)]
    total_price = store.order(shopping_list)

    assert total_price == 625
    assert non_stocked_prod.quantity is None