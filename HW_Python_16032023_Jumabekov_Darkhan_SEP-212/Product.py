'''
Задание 2
Реализуйте класс "Товар".
Необходимо хранить в переменных-членах класса:
- название товара,
- фирма изготовитель,
- цена,
- количество товара на складе,
- описание.
'''

from random import randint
from random import choice

products_name = ['Milk', 'Bread', 'Butter', 'Potatoes', 'Apples', 'Tea', 'Onions']
manufacturers_name = ['Rodina', 'Cesna', 'President', 'Small', 'Magnum', 'Champion', 'Bazar']


class Product:
    __name: str
    __manufacturer: str
    __price: float
    __count: int
    __description: str

    def __init__(self) -> None:
        pass

    @property
    def name(self): return self.__name

    @property
    def manufacturer(self): return self.__manufacturer

    @property
    def price(self): return self.__price

    @property
    def count(self): return self.__count

    @property
    def description(self): return self.__description

    @name.setter
    def name(self, name): self.__name = name

    @manufacturer.setter
    def manufacturer(self, manufacturer): self.__manufacturer = manufacturer

    @price.setter
    def price(self, price): self.__price = price

    @count.setter
    def count(self, count): self.__count = count

    @description.setter
    def description(self, description): self.__description = description

    def input(self):
        self.name = input('Enter product name: ')
        self.manufacturer = input('Enter manufacturer: ')
        self.price = float(input('Enter price: '))
        self.count = int(input('Enter count: '))
        self.description = input('Enter description: ')
        return self

    def rand(self):
        self.name = choice(products_name)
        self.manufacturer = choice(manufacturers_name)
        self.price = float(randint(300, 3000))
        self.count = randint(1, 100)
        self.description = ''.join(chr(randint(ord('a'), ord('z'))) for x in range(randint(7, 17)))
        return self

    def __eq__(self, right) -> bool:
        if self.name == right.name and \
                self.manufacturer == right.manufacturer and \
                self.price == right.price and \
                self.count == right.count and \
                self.description == right.description:
            return True
        return False

    def __repr__(self):
        return f'{self.name} -- {self.manufacturer} -- {self.price} -- {self.count} -- {self.description}'
