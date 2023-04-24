import sys

from Product import Product
from DB import DB

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
    __db: DB

    def __init__(self) -> None:
        pass

    def __init__(self, name: str, db: DB):
        self.__name = name
        self.__db = db

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def input(self, count: int):
        for _ in range(count):
            product = Product()
            product.input()
            self.__db.insert(product)

    def rand(self, count: int):
        for _ in range(count):
            product = Product()
            p = product.rand()
            self.__db.insert(p)

    def copy(self):
        store = Store()
        store.name = self.name
        store.products = self.products.copy()
        return store

    def __str__(self) -> str:
        s = ''
        selected_products = self.__db.readAll()
        if selected_products is not None:
            for product in selected_products:
                product = Product().convert_to_product(id=product[0], name=product[1], manufacturer=product[2], \
                                                       price=product[3], count=product[4], \
                                                       description=product[5])
                s += f'{product} \n'
        return s

    def printProductsByPrice(self, from_price: float, to_price: float) -> str:
        s = ''
        if isinstance(from_price, float) and isinstance(to_price, float):
            if from_price > 0 and to_price < sys.float_info.max:
                selected_products = self.__db.getProductsByPrice(from_price, to_price)
                if selected_products is not None:
                    for product in selected_products:
                        product = Product().convert_to_product(id=product[0], name=product[1], manufacturer=product[2], \
                                                               price=product[3], count=product[4], \
                                                               description=product[5])
                        s += f'{product} \n'
        return s

    def findProductByParam(self, param: str, column: str):
        s = ''
        selected_products = self.__db.getProductByParam(param, column)
        if selected_products is not None:
            for product in selected_products:
                product = Product().convert_to_product(id=product[0], name=product[1], manufacturer=product[2], \
                                                       price=product[3], count=product[4], \
                                                       description=product[5])
                s += f'{product} \n'
        return s

    def sortProductsByParam(self, param: str):
        s = ''
        if isinstance(param, str):
            selected_products = self.__db.sortProductsByParam(param)
            if selected_products is not None:
                for product in selected_products:
                    product = Product().convert_to_product(id=product[0], name=product[1], manufacturer=product[2], \
                                                           price=product[3], count=product[4], \
                                                           description=product[5])
                    s += f'{product} \n'
        return s

    def __add__(self, otherProduct):
        self.__db.insert(otherProduct)

    def __sub__(self, product):
        id = self.__db.readOne(product)[0][0]
        if id > 0:
            self.__db.delete(id)

    def deleteById(self, id):
        id = self.__db.getById(id)[0][0]
        if id > 0:
            self.__db.delete(id)
