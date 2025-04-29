from __future__ import annotations
from typing import List, Dict, Any


class Product:
    """
    name, description, price (>0), quantity (>=0)
    Поддерживает вызовы:
        Product(name, price, quantity [, description])
        Product(name, description, price, quantity)
    """

    def __init__(self, name: str, *args):
        if len(args) < 2:
            raise TypeError(
                "Нужно минимум три позиционных аргумента: "
                "name, price, quantity  (или  name, description, price, quantity)"
            )

        # вариант 1: (name, price, quantity, [description])
        if isinstance(args[0], (int, float)):
            price, quantity = args[0], args[1]
            description = args[2] if len(args) > 2 else ""
        # вариант 2: (name, description, price, quantity)
        else:
            description, price, quantity = args[0], args[1], args[2]

        if price <= 0 or quantity < 0:
            raise ValueError("Цена должна быть положительной, количество — неотрицательным")

        self.name: str = name
        self.description: str = description
        self.__price: float = float(price)          # приватное хранение цены
        self.quantity: int = int(quantity)

    # ─────────────────────  price property  ───────────────────── #

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float | int) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = float(value)

    # ─────────────────────  helpers  ───────────────────── #

    @classmethod
    def new_product(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            data["name"],
            data.get("description", ""),
            data["price"],
            data["quantity"],
        )

    def __str__(self) -> str:
        price_view = int(self.price) if self.price.is_integer() else round(self.price, 2)
        return f"{self.name}, {price_view} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        return f"Product({self.name!r}, {self.price}, {self.quantity})"

    # ─────────────────────  арифметика  ───────────────────── #

    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity


class Category:
    """
    category_count  – количество созданных категорий
    products_count  – суммарное количество товаров во всех категориях
    """

    category_count: int = 0
    products_count: int = 0

    def __init__(self, name: str, description: str = "", products: List[Product] | None = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = list(products) if products else []

        Category.category_count += 1
        Category.products_count += sum(p.quantity for p in self.__products)

    # ─────────────────────  работа с товарами  ───────────────────── #

    @property
    def products(self) -> str:
        """Человекочитаемый список продуктов (строки через \n, + перевод строки в конце)."""
        if not self.__products:
            return ""
        return "\n".join(map(str, self.__products)) + "\n"

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")
        self.__products.append(product)
        Category.products_count += product.quantity

    # ─────────────────────  iter, len, str, repr  ───────────────────── #

    def __iter__(self):
        return iter(self.__products)

    def __len__(self) -> int:
        return len(self.__products)

    def __str__(self) -> str:
        total_qty = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_qty} шт."

    def __repr__(self) -> str:
        return f"Category({self.name!r}, products={len(self)})"