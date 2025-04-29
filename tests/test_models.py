# tests/test_models.py
import pytest
from src.models import Category, Product


def _reset_counters() -> None:
    """Обнуляем глобальные счётчики перед тестами, чтобы они были детерминированными."""
    Category.category_count = 0
    Category.products_count = 0


def test_product_initialization() -> None:
    item = Product("Колонка", 8_490, 10, "Умная колонка")

    assert item.name == "Колонка"
    assert item.price == 8_490
    assert item.quantity == 10
    assert item.description == "Умная колонка"


def test_category_initialization_counts() -> None:
    _reset_counters()

    book = Product("Книга", 2_000, 5, "Clean Code")
    mouse = Product("Мышь", 7_000, 2, "Logitech MX Master")

    cat = Category("Разное", "Книги и аксессуары", [book, mouse])

    assert cat.name == "Разное"
    # количество товаров определяем через len(category),
    # так как products — человекочитаемая строка
    assert len(cat) == 2

    assert Category.category_count == 1
    assert Category.products_count == 2

    expected = (
        "Книга, 2000.0 руб. Остаток: 5 шт.\n"
        "Мышь, 7000.0 руб. Остаток: 2 шт.\n"
    )
    assert cat.products == expected


def test_add_product_updates_counter() -> None:
    _reset_counters()

    cat = Category("Одежда", "Мужская одежда")
    assert Category.products_count == 0

    tshirt = Product("Футболка", 1_799, 30, "100 % cotton")
    cat.add_product(tshirt)

    assert len(cat) == 1
    assert Category.products_count == 1
    assert cat.products == "Футболка, 1799.0 руб. Остаток: 30 шт.\n"


@pytest.mark.parametrize("bad_price", [-1, -100.5])
def test_product_negative_price_validation(bad_price, capsys) -> None:
    """
    При попытке установить отрицательную цену выводится предупреждение,
    а цена остаётся прежней.
    """
    item = Product("Bad", 1_000, 1)
    start_price = item.price

    item.price = bad_price
    captured = capsys.readouterr().out.strip()

    assert captured == "Цена не должна быть нулевая или отрицательная"
    assert item.price == start_price