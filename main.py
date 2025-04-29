from __future__ import annotations

from src.models import Category, Product

if __name__ == "__main__":
    phone = Product("iPhone 15", "Смартфон 128 ГБ", 110_000, 5)
    mac = Product("MacBook Air M2", "Ноутбук 13″", 135_000, 3)

    gadgets = Category("Электроника", "Гаджеты Apple", [phone, mac])

    print(gadgets)  # Category('Электроника', items=2)
    print(Category.category_count)  # 1
    print(Category.product_count)  # 2

    # main.py

    class Product:

        def __init__(self, name: str, price: float, quantity: int = 0) -> None:
            self.name = name
            self.quantity = quantity
            self.price = price

        @property
        def price(self) -> float:
            return self.__price

        @price.setter
        def price(self, new_price: float) -> None:


            if new_price > 0:
                self.__price = new_price
            else:
                print("Цена не должна быть нулевая или отрицательная")

        def __repr__(self) -> str:  # удобно для отладки и тестов
            return f"Product({self.name!r}, {self.price}, {self.quantity})"

        @classmethod
        def new_product(cls, data: dict[str, object]) -> "Product":

            return cls(
                name=data["name"],
                price=data["price"],
                quantity=data.get("quantity", 0),
            )


    class Category:

        products_count = 0

        def __init__(self, name: str) -> None:
            self.name = name
            self.__products: list[Product] = []

        # ---------- работа со списком товаров ----------
        def add_product(self, product: Product) -> None:

            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только экземпляры Product")
            self.__products.append(product)
            Category.products_count += 1

        @property
        def products(self) -> str:

            return "".join(
                f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
                for p in self.__products
            )

        def __repr__(self) -> str:
            return f"Category({self.name!r}, {len(self.__products)} товаров)"
