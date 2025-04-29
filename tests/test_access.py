import pytest
from src.models import Category, Product


def _reset():
    Category.category_count = 0
    Category.products_count = 0


def test_add_product_and_counter():
    _reset()

    cat = Category("Смартфоны")
    phone = Product("iPhone 15 Pro", 149_990, 5)

    cat.add_product(phone)

    assert cat.products == "iPhone 15 Pro, 149990 руб. Остаток: 5 шт.\n"
    assert Category.category_count == 1
    assert Category.products_count == 5
    assert len(cat) == 1


def test_price_setter_positive_value():
    p = Product("MacBook Air", 120_000, 3)
    p.price = 130_000
    assert p.price == 130_000


def test_price_setter_negative_value(capsys):
    p = Product("Mouse", 3_300, 2)
    p.price = -10
    assert capsys.readouterr().out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert p.price == 3_300


def test_classmethod_new_product():
    data = {"name": "AirPods Pro", "price": 24_990, "quantity": 10}
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.price == 24_990
    assert p.quantity == 10