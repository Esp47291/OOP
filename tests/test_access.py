# tests/test_access.py
import pytest
from src.models import Category, Product


def _reset_counters() -> None:
    """Обнуляем глобальные счётчики, чтобы тесты были независимы друг от друга."""
    Category.category_count = 0
    Category.products_count = 0


def test_add_product_and_counter() -> None:
    _reset_counters()

    cat = Category("Смартфоны")
    phone = Product("iPhone 15 Pro", 149_990, 5)

    cat.add_product(phone)

    # строка-представление списка товаров
    expected = "iPhone 15 Pro, 149990.0 руб. Остаток: 5 шт.\n"
    assert cat.products == expected

    # проверяем счётчики
    assert Category.category_count == 1
    assert Category.products_count == 1
    assert len(cat) == 1


def test_price_setter_positive_value() -> None:
    p = Product("Macbook Air", 120_000, 3)
    p.price = 130_000
    assert p.price == 130_000


def test_price_setter_negative_value(capsys) -> None:
    p = Product("Mouse", 3_300, 2)
    p.price = -10

    captured = capsys.readouterr().out.strip()
    assert captured == "Цена не должна быть нулевая или отрицательная"
    assert p.price == 3_300  # цена не изменилась


def test_classmethod_new_product() -> None:
    data = {"name": "AirPods Pro", "price": 24_990, "quantity": 10}
    p = Product.new_product(data)

    assert isinstance(p, Product)
    assert p.name == "AirPods Pro"
    assert p.price == 24_990
    assert p.quantity == 10