from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Any


class Product:
    """
    Товар интернет-магазина.

    Параметры
    ---------
    name : str
        Название товара.
    price : float | int
        Цена (> 0). Значение хранится в приватном атрибуте ``__price``.
    quantity : int
        Количество (> 0).
    description : str, optional
        Описание товара.
    """

    # ──────────────────────────── инициализация ───────────────────────────── #

    def __init__(
        self,
        name: str,
        price: float | int,
        quantity: int,
        description: str = "",
    ) -> None:
        if price <= 0 or quantity < 0:
            raise ValueError("Цена и количество должны быть положительными")

        self.name = name
        self.description = description
        self.__price: float = float(price)        # приватный атрибут
        self.quantity: int = int(quantity)

    # ──────────────────────────── price: property ─────────────────────────── #

    @property
    def price(self) -> float:
        """Текущая цена товара (read-only для прямого доступа)."""
        return self.__price

    @price.setter
    def price(self, value: float | int) -> None:
        """
        Меняет цену товара.  При нулевом или отрицательном значении
        выводит предупреждение и не меняет цену.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = float(value)

    # ───────────────────────── class-method helper ────────────────────────── #

    @classmethod
    def new_product(cls, data: Dict[str, Any]) -> "Product":
        """
        Создаёт товар из словаря::

            data = {
                "name": "AirPods",
                "price": 24990,
                "quantity": 10,
                "description": "TWS-наушники",
            }
        """
        return cls(
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"],
            description=data.get("description", ""),
        )

    # ─────────────────────────────── служебное ────────────────────────────── #

    def __repr__(self) -> str:
        return f"Product({self.name!r}, {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    """
    Категория товаров.

    Параметры
    ---------
    name : str
        Название категории.
    description : str
        Описание.
    products : list[Product] | None
        Стартовый список товаров.

    Класс-атрибуты
    --------------
    category_count : int
        Сколько категорий создано.
    products_count : int
        Сколько товаров во всех категориях.
    """

    category_count: int = 0
    products_count: int = 0

    # ──────────────────────────── инициализация ───────────────────────────── #

    def __init__(
        self,
        name: str,
        description: str = "",
        products: List[Product] | None = None,
    ) -> None:
        self.name = name
        self.description = description
        # приватный список товаров
        self.__products: List[Product] = list(products) if products else []

        Category.category_count += 1
        Category.products_count += len(self.__products)

    # ──────────────────────────── products: getter ────────────────────────── #

    @property
    def products(self) -> str:
        """
        Возвращает список товаров в человекочитаемом формате::

            iPhone 15 Pro, 149990 руб. Остаток: 5 шт.
            …
        """
        if not self.__products:
            return ""
        lines = [str(item) for item in self.__products]
        # по заданию - перевод строки в конце строки
        return "\n".join(lines) + "\n"

    # ────────────────────────── работа с товарами ─────────────────────────── #

    def add_product(self, product: Product) -> None:
        """Добавить товар в категорию и обновить счётчик."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")

        self.__products.append(product)
        Category.products_count += 1

    # ─────────────────────────────── служебное ────────────────────────────── #

    def __len__(self) -> int:
        """len(category) &rarr; количество товаров."""
        return len(self.__products)

    def __repr__(self) -> str:
        return f"Category({self.name!r}, products={len(self)})"

    def __str__(self) -> str:
        return f"{self.name} ({len(self)} поз.)"