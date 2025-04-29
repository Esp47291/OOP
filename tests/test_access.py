# tests/test_access.py
import pytest

# импортируем классы напрямую из пакета src,
# чтобы использовать их фактическую реализацию
from src.models import Product, Category


def test_add_product_and_counter():
    # Сохраняем текущие значения счётчиков,
    # чтобы тест был независим от других.
    start_category_count = Category.category_count
    start_product_count = Category.product_count

    cat = Category("Смартфоны")
    phone = Product("iPhone 15 Pro", 149990, 5)
    cat.add_product(phone)

    # В категории теперь ровно один товар ‒ тот, что мы добавили
    assert len(cat) == 1
    assert cat.products[0] is phone

    # Проверяем, что глобальные счётчики увеличились
    assert Category.category_count == start_category_count + 1
    assert Category.product_count == start_product_count + 1


def test_price_setter_positive_value():
    p = Product("Macbook Air", 120000, 3)
    p.price = 130000
    assert p.price == 130000


def test_price_setter_negative_value(capsys):
    p = Product("Mouse", 3300)
    p.price = -10

    captured = capsys.readouterr().out.strip()
    assert captured == "Цена должна быть неотрицательной"
    # Цена не изменилась
    assert p.price == 3300


def test_classmethod_new_product():
    data = {"name": "AirPods Pro", "price": 24990, "quantity": 10}
    p = Product.new_product(data)

    assert isinstance(p, Product)
    assert p.name == "AirPods Pro"
    assert p.price == 24990
    assert p.quantity == 10