from __future__ import annotations
from typing import List, Dict, Any


class Product:
    """
    Модель товара интернет-магазина.
    name         – название
    price        – цена (неотрицательная)
    quantity     – количество на складе
    description  – произвольное текстовое описание
    """

    def __init__(
        self,
        name: str,
        price: float,
        quantity: int = 0,
        description: str = ""
    ) -> None:
        self.name = name
        self.description = description
        self._price: float = 0          # будет задан через setter
        self.price = price              # валидация
        self.quantity = int(quantity)

    # &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; price (property) &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; #

    @property
    def price(self) -> float:
        """Текущая цена товара."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """
        Меняем цену товара.  При отрицательном значении
        выводим сообщение и не изменяем текущее значение.
        """
        if value < 0:
            # именно print – в тестах проверяется вывод через capsys
            print("Цена должна быть неотрицательной")
            return
        self._price = float(value)

    # &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; classmethod new_product &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; #

    @classmethod
    def new_product(cls, data: Dict[str, Any]) -> "Product":
        """
        Создаёт товар из словаря:
            {"name": "...", "price": 123, "quantity": 4, "description": "..."}
        Поля quantity и description необязательны.
        """
        return cls(
            name=data["name"],
            price=data["price"],
            quantity=data.get("quantity", 0),
            description=data.get("description", "")
        )

    # &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; служебные методы &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; #

    def __repr__(self) -> str:                  # для отладки
        return f"Product({self.name!r}, {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name} – ${self.price:.2f} ({self.quantity} шт.)"


class Category:
    """
    Категория товаров.

    Атрибуты экземпляра:
        name        – название категории
        description – описание
        products    – список Product

    Атрибуты класса:
        category_count – сколько всего категорий создано
        product_count  – сколько всего товаров во всех категориях
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str = "",
        products: List[Product] | None = None
    ) -> None:
        self.name = name
        self.description = description
        self.products: List[Product] = list(products) if products else []

        # Cчётчики классов
        Category.category_count += 1
        Category.product_count += len(self.products)

    # &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; работа с товарами &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; #

    def add_product(self, product: Product) -> None:
        """Добавить товар в категорию и увеличить общий счётчик."""
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты Product")
        self.products.append(product)
        Category.product_count += 1

    # &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; служебные методы &mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; #

    def __len__(self) -> int:
        """Количество товаров в категории (len(category))."""
        return len(self.products)

    def __repr__(self) -> str:
        return f"Category({self.name!r}, products={len(self)})"

    def __str__(self) -> str:
        return f"{self.name} ({len(self)} позиций)"