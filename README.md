## Что реализовано

* **Product** – сущность товар с атрибутами `name, description, price, quantity`.
* **Category** – каталог товаров.  
  При создании объекта автоматически увеличиваются счётчики:
  * `Category.category_count` – сколько всего категорий,
  * `Category.product_count` – суммарное число товаров во всех категориях.

Покрытие тестами (pytest + pytest-cov) > 75 %, код соответствует PEP-8 (flake8 &le; 5 ошибок).