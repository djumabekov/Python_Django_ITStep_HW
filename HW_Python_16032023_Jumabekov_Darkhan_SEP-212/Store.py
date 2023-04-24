import sys
from operator import attrgetter
from Product import Product

'''
Задание 2
Создайте класс "Магазин", который бдет хранить и управлять списком объектов "Товар".
Для работы с классом массивом "Магазин" необходимо реализовать:
- Ввод данных с консоли для товаров Магазина.
- Случайное (рандомное) заполнение товаров в массиве Магазина.
- Печать всех товаров из класса Магазин.
- Печать только тех товаров, цена которых лежит в указанном диапазоне. Диапазон цен вводит пользователь.
- Поиск товара по названию товара.
- Поиск товара по названию фирмы изготовителя.
- Сортировка массива товаров по названию товара.
- Сортировка массива товаров по цене товара.
- Добавление и удаление товара из класса "Магазин"
'''

class Store:
    __name: str
    __products = []

    def __init__(self) -> None:
        pass

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def products(self):
        return self.__products

    @name.setter
    def name(self, name):
        self.__name = name

    @products.setter
    def products(self, products):
        self.__products = products

    def input(self, count: int):
        for _ in range(count):
            product = Product()
            product.input()
            self.products.append(product)

    def rand(self, count: int):
        for _ in range(count):
            product = Product()
            self.products.append(product.rand())

    def copy(self):
        store = Store()
        store.name = self.name
        store.products = self.products.copy()
        return store

    def __str__(self) -> str:
        s = ''
        for product in self.products:
            s += f'{product} \n'
        return s

    def printProductsByPrice(self, from_price: float, to_price: float) -> str:
        s = ''
        if from_price > 0 and to_price < sys.float_info.max:
            for product in self.products:
                if from_price <= product.price <= to_price:
                    s += f'{product} \n'
        return s

    def findProductByName(self, name: str) -> Product:
        product = [str(product) for product in self.products if product.name.lower().strip().__contains__(name.lower().strip())]
        if product:
            return product
        return None

    def findProductByManufacturer(self, manufacturer: str) -> Product:
        product = [str(product) for product in self.products if product.manufacturer.lower().strip().__contains__(manufacturer.lower().strip())]
        if product:
            return product
        return None

    def sortProductsByName(self):
        products_copy = self.products.copy()
        sorted_by_name = sorted(products_copy, key=lambda x: x.name.lower())
        return sorted_by_name

    def sortProductsByPrice(self):
        products_copy = self.products.copy()
        sorted_by_price = sorted(products_copy, key=lambda x: x.price)
        return sorted_by_price

    def __add__(self, otherProduct):
        self.products.append(otherProduct)

    def __sub__(self, product):
        filtered_products = [p for p in self.products if p != product]
        self.products = filtered_products
