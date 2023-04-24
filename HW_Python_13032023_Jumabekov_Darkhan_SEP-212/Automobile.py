'''
Задание №1
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели,
год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''

class Automobile:
    __model: str
    __year: int
    __manufacturer: str
    __engine: float
    __color: str
    __price: float

    def __init__(self, model, year, manufacturer, engine, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    @property
    def model(self): return self.__model
    @property
    def year(self): return self.__year
    @property
    def manufacturer(self): return self.__manufacturer
    @property
    def engine(self): return self.__engine
    @property
    def color(self): return self.__color
    @property
    def price(self): return self.__price

    @model.setter
    def model(self, model): self.__model = model
    @year.setter
    def year(self, year): self.__year = year
    @manufacturer.setter
    def manufacturer(self, manufacturer): self.__manufacturer = manufacturer
    @engine.setter
    def engine(self, engine): self.__engine = engine
    @color.setter
    def color(self, color): self.__color = color
    @price.setter
    def price(self, price): self.__price = price

    def __str__(self):
        return f'{self.model} \
        | {self.year} \
        | {self.manufacturer} \
        | {self.engine} \
        | {self.color} \
        | {self.price}'

    def input(self):
        self.model = input('Enter model: ')
        self.year = input('Enter year: ')
        self.manufacturer = input('Enter manufacturer: ')
        self.engine = input('Enter engine: ')
        self.color = input('Enter color: ')
        self.price = input('Enter price: ')

