'''
Задание №2
Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год
выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода
данных, реализуйте доступ к отдельным полям через методы класса.
'''

class Book:
    __name: str
    __year: int
    __publisher: str
    __genre: str
    __author: str
    __price: float

    def __init__(self, *args, **kwargs):
        keys = ['name', 'year', 'publisher', 'genre', 'author', 'price']
        for key in kwargs:
            try:
                idx = keys.index(str(key))
            except:
                idx = -1  # недействительный ключ, атрибут

            match idx:
                case 0:  # 'name'
                    self.name = kwargs[key]
                case 1:  # 'year'
                    self.year = kwargs[key]
                case 2:  # 'publisher'
                    self.publisher = kwargs[key]
                case 3:  # 'genre'
                    self.genre = kwargs[key]
                case 4:  # 'author'
                    self.author = kwargs[key]
                case 5:  # 'price'
                    self.price = kwargs[key]
                case _:  # default:
                    print('Неверный парамер ' + str(key))

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @property
    def publisher(self):
        return self.__publisher

    @property
    def genre(self):
        return self.__genre

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, name):
        self.__name = name

    @year.setter
    def year(self, year):
        self.__year = year

    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @author.setter
    def author(self, author):
        self.__author = author

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return f'{self.name} \
           | {self.year} \
           | {self.publisher} \
           | {self.genre} \
           | {self.author} \
           | {self.price}'

    def input(self):
        self.name = input('Enter name: ')
        self.year = input('Enter year: ')
        self.publisher = input('Enter publisher: ')
        self.genre = input('Enter genre: ')
        self.author = input('Enter author: ')
        self.price = input('Enter price: ')