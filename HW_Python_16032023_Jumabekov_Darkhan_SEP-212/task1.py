'''
a) Опишите класс Книга: Автор, название, год, цена.
Создайте класс Библиотека.
Класс предназначен для хранения информации о библиотеке:
название, адрес, книги.

b) Реализуйте необходимые для класса методы.
Используя перегрузку операторов реализуйте
для него следующие арифметические операции:
+ добавляет к количеству книг указанное значение;
- вычитает из количества книг указанное значение;
+= добавляет к количеству книг указанное значение;
-= вычитает из количества книг указанное значение;
Используя перегрузку операторов реализуйте
(сравнение по количеству книг):<;>;<=;>=;==;!=
__len__, __getitem__, ....
'''
from random import random
from random import randint
from random import choice

authName = ['Jho', 'Mike', 'Pushkin', 'Eminame']


class Book(object):
    __author = ''
    __name = ''
    __year = 0
    __price = ''

    def __init__(self, author, name):
        self.__author = author
        self.__name = name

    def __init__(self, a, n, y, p):
        self.__author = a
        self.__name = n
        self.__year = y
        self.__price = p

    def __init__(self) -> None:
        pass

    # def __init__(self, *args, **kwarg):
    #  pass
    @property
    def Author(self):
        return self.__author

    @property
    def Name(self):
        return self.__name

    @property
    def Year(self):
        return self.__year

    @property
    def Price(self):
        return self.__price

    @Author.setter
    def Author(self, val):
        self.__author = val

    @Name.setter
    def Name(self, val):
        self.__name = val

    @Year.setter
    def Year(self, val):
        self.__year = val

    @Price.setter
    def Price(self, val):
        self.__price = val

    @property
    def rand(self):
        self.Author = choice(authName)
        size = randint(3, 10)
        self.Name = ''.join(chr(randint(ord('A'), ord('Z'))) \
                            for a in range(size))
        self.Year = randint(1600, 2023)
        self.Price = randint(100, 1000)
        return self

    def __ne__(self, right) -> bool:
        if self.Author != right.Author or \
                self.Name != right.Name or \
                self.Year != right.Year or \
                self.Price != right.Price:
            return True

        return False

    def __eq__(self, right) -> bool:
        if self.Author == right.Author and \
                self.Name == right.Name and \
                self.Year == right.Year and \
                self.Price == right.Price:
            return True

        return False

    def __str__(self) -> str:
        # return '\t'.join(str(a) for a in \
        # (self.__name ,self.__author,\
        #  self.__year,self.__price ))
        s = ''
        s += '{:>11}'.format(self.Name)
        s += '{:^12}'.format(self.Author)
        s += '{:5}'.format(self.Year)
        s += '{:6}'.format(self.Price)
        return s


class Library(object):
    __books = []
    __addr = ''
    __name = ''

    def __init__(self) -> None:
        pass

    def __init__(self, count: int):
        for x in range(count):
            temp = Book()
            temp.rand
            self.__books.append(temp)

    @property
    def Addr(self):
        return self.__addr

    @property
    def Name(self):
        return self.__name

    @property
    def Books(self):
        return self.__books

    @Books.setter
    def Books(self, val):
        self.__books = val.copy()

    @Name.setter
    def Name(self, val):
        self.__name = val

    @Addr.setter
    def Addr(self, val):
        self.__addr = val

    def __str__(self):
        s = ''
        s += self.Addr + '\n'
        s += self.Name + '\n'
        for b in self.Books:
            s += str(b) + ' \n'

        return s;

    def copy(self):
        l = Library(0)
        l.Name = self.Name
        l.Addr = self.Addr
        l.Books = self.Books.copy()
        return l

    def __add__(self, val):
        if type(val) == type(Book()):
            l = self.copy()
            l.Books.append(val)
            return l
        elif type(val) == type(int()):
            # b = Book()
            l = self.copy()
            for x in range(val):
                # l.Books.append(b.rand)
                l.Books.append(Book().rand)
            return l
        return None

    def __sub__(self, val):
        if type(val) != type(Book()):
            return None
        # assert type(val) == type(Book()) return None
        l = self.copy()
        l.Books = [b for b in l.Books if b != val]
        return l


def task1():
    l = Library(5)
    print('\nOriginal list from library:', l)

    r = Book()  # 'Ronaldo', 'Goal')#,2023,255)
    r.Author = 'Ronaldo'
    r.Name = 'Goal'
    r.Year = 2023
    r.Price = 500

    l2 = l + r
    print(f'\nCopy list from library with added new book {r}:', l2)
    print()
    print('\nOriginal list from library:', l)
    l2 = l2 + 4
    print(f'\nCopy list from library with added 4 new book:', l2)

    # Ошибка в работе - неверно удаляет книгу из библиотеки
    l2 = l2 - r
    print('\nCopy list from library with deleted new book:')
    print(f'\nудаляем книгу {r} из библиотеки:', l2)

    m = Book()  # 'Ronaldo', 'Goal')#,2023,255)
    m.Author = 'Messi'
    m.Name = 'Leonel'
    m.Year = 1988
    m.Price = 5000

    l2 = l2 + m
    print(f'\nCopy list from library with added new book {m}:', l2)

    l2 = l2 - m
    print(f'\nCopy list from library with deleted new book {m}:')
    print(f'\nудаляем книгу {m} из библиотеки:', l2)
