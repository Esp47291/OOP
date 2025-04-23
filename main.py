from src.models import Category, Product

if __name__ == "__main__":
    phone = Product("iPhone 15", "Смартфон 128 ГБ", 110_000, 5)
    mac = Product("MacBook Air M2", "Ноутбук 13″", 135_000, 3)

    gadgets = Category("Электроника", "Гаджеты Apple", [phone, mac])

    print(gadgets)  # Category('Электроника', items=2)
    print(Category.category_count)  # 1
    print(Category.product_count)  # 2
