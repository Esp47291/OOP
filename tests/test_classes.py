import pytest
from main import Smartphone, LawnGrass, Category, Product

@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0

def test_product_initialization():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10

def test_category_initialization():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2

def test_add_product():
    category = Category("Test Category", "Test Description")
    product = Product("Test Product", "Test Description", 100.0, 10)
    category.add_product(product)
    assert len(category._Category__products) == 1
    assert Category.product_count == 1

def test_add_product_type_check():
    category = Category("Test Category", "Test Description")
    with pytest.raises(TypeError):
        category.add_product("Not a Product")

def test_products_getter():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category = Category("Test Category", "Test Description", [product1, product2])
    expected_output = (
        "Product 1, 100.0 руб. Остаток: 5 шт.\n"
        "Product 2, 200.0 руб. Остаток: 3 шт."
    )
    assert category.products == expected_output

def test_new_product():
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 10
    }
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10

def test_price_setter():
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = 200.0
    assert product.price == 200.0
    product.price = -50.0
    assert product.price == 200.0  # Price should not change
    product.price = 0
    assert product.price == 200.0  # Price should not change

def test_multiple_categories():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    product3 = Product("Product 3", "Description 3", 300.0, 2)
    category1 = Category("Category 1", "Description 1", [product1, product2])
    category2 = Category("Category 2", "Description 2", [product3])
    assert Category.category_count == 2
    assert Category.product_count == 3

def test_price_setter_with_zero():
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = 0
    assert product.price == 100.0  # Price should not change

def test_price_setter_with_negative():
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = -10
    assert product.price == 100.0  # Price should not change

def test_category_add_product_increments_product_count():
    category = Category("Test Category", "Test Description")
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category.add_product(product1)
    category.add_product(product2)
    assert Category.product_count == 2

def test_category_initialization_with_empty_products_list():
    category = Category("Test Category", "Test Description", [])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category._Category__products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0

def test_category_add_product_with_invalid_type():
    category = Category("Test Category", "Test Description")
    with pytest.raises(TypeError):
        category.add_product("Invalid Product")

def test_category_products_getter_with_no_products():
    category = Category("Test Category", "Test Description")
    assert category.products == ""

def test_product_str():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_category_str():
    category = Category("Test Category", "Test Description")
    assert str(category) == "Test Category, количество продуктов: 0 шт."


def test_product_addition():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    total_price = product1 + product2
    assert total_price == 100.0 * 5 + 200.0 * 3


def test_smartphone_str():
    smartphone = Smartphone("Test Smartphone", "Description", 1000.0, 10, 95.5, "ModelX", 128, "Black")
    expected_str = ("Test Smartphone, Модель: ModelX, Производительность: 95.5, "
                     "Память: 128, Цвет: Black, 1000.0 руб. Остаток: 10 шт.")
    assert str(smartphone) == expected_str


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass("Test Grass", "Description", 500.0, 20, "Country", "7 days", "Green")
    assert lawn_grass.name == "Test Grass"
    assert lawn_grass.description == "Description"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Country"
    assert lawn_grass.germination_period == "7 days"
    assert lawn_grass.color == "Green"


def test_lawn_grass_str():
    lawn_grass = LawnGrass("Test Grass", "Description", 500.0, 20, "Country", "7 days", "Green")
    expected_str = ("Test Grass, Страна: Country, Срок прорастания: 7 days дней, "
                     "Цвет: Green, 500.0 руб. Остаток: 20 шт.")
    assert str(lawn_grass) == expected_str


def test_addition_of_smartphones():
    smartphone1 = Smartphone("Smartphone 1", "Description 1", 1000.0, 10, 95.5, "ModelX", 128, "Black")
    smartphone2 = Smartphone("Smartphone 2", "Description 2", 1500.0, 5, 98.0, "ModelY", 256, "White")
    total_price = smartphone1 + smartphone2
    assert total_price == 1000.0 * 10 + 1500.0 * 5


def test_addition_of_lawn_grass():
    grass1 = LawnGrass("Grass 1", "Description 1", 500.0, 20, "Country1", "7 days", "Green")
    grass2 = LawnGrass("Grass 2", "Description 2", 400.0, 15, "Country2", "5 days", "Dark Green")
    total_price = grass1 + grass2
    assert total_price == 500.0 * 20 + 400.0 * 15


def test_product_repr():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert repr(product) == "Product, (Test Product, Test Description, 100.0, 10)"


def test_logging_mixin_output(capsys):
    product = Product("Test Product", "Test Description", 100.0, 10)
    captured = capsys.readouterr()
    assert "Product, (Test Product, Test Description, 100.0, 10)" in captured.out


@pytest.fixture
def sample_products():
    """Фикстура с тестовыми продуктами разной цены"""
    return [
        Product("Product 1", "Desc 1", 100.0, 2),
        Product("Product 2", "Desc 2", 200.0, 3),
        Product("Product 3", "Desc 3", 300.0, 1)
    ]


def test_zero_quantity_product():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Zero Product", "Description", 50.0, 0)


def test_middle_price_empty_category():
    category = Category("Empty Category", "Empty Desc", [])
    assert category.middle_price() == 0

