# tests/test_access.py
import builtins
import types
import pytest
from main import Product, Category


def test_add_product_and_counter():
    cat = Category("Смартфоны")
    phone = Product("iPhone 15 Pro", 149990, 5)

    cat.add_product(phone)

    # приватный список напрямую недоступен
    assert not hasattr(cat, "products")
    # but the property returns human-readable list
    expected = "iPhone 15 Pro, 149990 руб. Остаток: 5 шт.\n"
    assert cat.products == expected
    assert Category.products_count == 1


def test_price_setter_positive_value():
    p = Product("Macbook Air", 120000, 3)
    p.price = 130000
    assert p.price == 130000


def test_price_setter_negative_value(capsys):
    p = Product("Mouse", 3300)
    p.price = -10
    captured = capsys.readouterr().out.strip()
    assert captured == "Цена не должна быть нулевая или отрицательная"
    assert p.price == 3300   # цена не изменилась


def test_classmethod_new_product():
    data = {"name": "AirPods Pro", "price": 24990, "quantity": 10}
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "AirPods Pro"
    assert p.price == 24990
    assert p.quantity == 10