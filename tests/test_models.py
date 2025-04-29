import pytest
from src.models import Category, Product


def _reset():
    Category.category_count = 0
    Category.products_count = 0


def test_product_str_and_add():
    a = Product("A", "desc", 100, 10)
    b = Product("B", "desc", 200, 2)

    assert str(a) == "A, 100 руб. Остаток: 10 шт."
    assert a + b == 100 * 10 + 200 * 2


def test_category_str_and_counts():
    _reset()
    book = Product("Книга", "Clean Code", 2_000, 5)
    mouse = Product("Мышь", "Logitech", 7_000, 2)

    cat = Category("Разное", "Книги и аксессуары", [book, mouse])

    assert str(cat) == "Разное, количество продуктов: 7 шт."
    assert Category.category_count == 1
    assert Category.products_count == 7
    assert cat.products == (
        "Книга, 2000 руб. Остаток: 5 шт.\n"
        "Мышь, 7000 руб. Остаток: 2 шт.\n"
    )


@pytest.mark.parametrize("bad_price", [0, -1, -100.5])
def test_product_bad_price_init(bad_price):
    with pytest.raises(ValueError):
        Product("Bad", "desc", bad_price, 1)