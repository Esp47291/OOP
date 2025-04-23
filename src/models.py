
from __future__ import annotations

from typing import List


class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if price <= 0:
            raise ValueError("Price must be > 0")
        if quantity < 0:
            raise ValueError("Quantity must be &ge; 0")

        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)

    def __repr__(self) -> str:  # pragma: no cover
        return f"Product({self.name!r}, price={self.price}, qty={self.quantity})"


class Category:

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product] | None = None) -> None:
        self.name = name
        self.description = description
        self.products: List[Product] = products or []

        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        Category.product_count += 1

    def __repr__(self) -> str:  # pragma: no cover
        return f"Category({self.name!r}, items={len(self.products)})"
