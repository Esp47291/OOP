import pytest
from src.models import Category, Product


def test_product_initialization() -> None:
    item = Product("Колонка", "Умная колонка", 8_490, 10)
    assert item.name == "Колонка"
    assert item.price == 8_490
    assert item.quantity == 10


def test_category_initialization_counts() -> None:
    # Сбрасываем счётчики (обычно так делать не нужно,
    # но в тестах удобно, чтобы значения были детерминированны).
    Category.category_count = 0
    Category.product_count = 0

    book = Product("Книга", "Clean Code", 2_000, 5)
    accel = Product("Мышь", "Logitech MX Master", 7_000, 2)

    cat = Category("Разное", "Книги и аксессуары", [book, accel])

    assert cat.name == "Разное"
    assert len(cat.products) == 2

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product_updates_counter() -> None:
    Category.category_count = 0
    Category.product_count = 0

    cat = Category("Одежда", "Мужская одежда")
    assert Category.product_count == 0

    tshirt = Product("Футболка", "Cotton", 1_799, 30)
    cat.add_product(tshirt)

    assert len(cat.products) == 1
    assert Category.product_count == 1


@pytest.mark.parametrize(
    "price, quantity",
    [
        (0, 1),  # цена ноль
        (-1, 1),  # цена отрицательная
        (1_000, -5),  # количество отрицательное
    ],
)
def test_product_validation(price, quantity) -> None:
    with pytest.raises(ValueError):
        Product("Bad", "Wrong data", price, quantity)
