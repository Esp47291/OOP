# tests/test_models.py
import pytest
from src.models import Category, Product


def test_product_initialization() -> None:
    """Корректная инициализация товара."""
    item = Product("Колонка", 8_490, 10, "Умная колонка")
    assert item.name == "Колонка"
    assert item.price == 8_490
    assert item.quantity == 10
    assert item.description == "Умная колонка"


def test_category_initialization_counts() -> None:
    """Создание категории увеличивает счётчики объектов и товаров."""
    # обнуляем счётчики, чтобы получить детерминированный результат
    Category.category_count = 0
    Category.product_count = 0

    book = Product("Книга", 2_000, 5, "Clean Code")
    mouse = Product("Мышь", 7_000, 2, "Logitech MX Master")

    cat = Category("Разное", "Книги и аксессуары", [book, mouse])

    assert cat.name == "Разное"
    assert len(cat.products) == 2

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product_updates_counter() -> None:
    """Добавление товара поправляет счётчик product_count."""
    Category.category_count = 0
    Category.product_count = 0

    cat = Category("Одежда", "Мужская одежда")
    assert Category.product_count == 0

    tshirt = Product("Футболка", 1_799, 30, "100 % cotton")
    cat.add_product(tshirt)

    assert len(cat.products) == 1
    assert Category.product_count == 1


@pytest.mark.parametrize(
    "bad_price",
    [-1, -100.5],
)
def test_product_negative_price_validation(bad_price, capsys) -> None:
    """
    При попытке установить отрицательную цену выводится предупреждение,
    а цена остаётся прежней.
    """
    item = Product("Bad", 1_000, 1)
    start_price = item.price
    item.price = bad_price

    captured = capsys.readouterr().out.strip()
    assert captured == "Цена должна быть неотрицательной"
    assert item.price == start_price