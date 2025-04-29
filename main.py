print(str(product1))
print(str(product2))
print(str(product3))

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3]
)

print(str(category1))

print(category1.products)

print(product1 + product2)
print(product1 + product3)
print(product2 + product3)