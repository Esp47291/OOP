from abc import ABC, abstractmethod
from itertools import product


class BaseProduct(ABC):
    @abstractmethod
    def __str__(self):
        pass

    def new_product(self):
        pass

    def __add__(self, other):
        pass

class LoggingMixin:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}, ({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, LoggingMixin):

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Операнд должен быть экземпляром того же класса")

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Добавляемый объект должен быть экземпляром класса Product или его наследника")

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.product_count} шт."

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"{self.name}, Модель: {self.model}, Производительность: {self.efficiency}, "
                f"Память: {self.memory}, Цвет: {self.color}, {self.price} руб. Остаток: {self.quantity} шт.")

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f"{self.name}, Страна: {self.country}, Срок прорастания: {self.germination_period} дней, "
                f"Цвет: {self.color}, {self.price} руб. Остаток: {self.quantity} шт.")
