'''
Задание 1
Создайте класс "Дробь".
Необходимо хранить в полях класса: числитель и знаменатель.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
Используя перегрузку операторов реализуйте для него арифметические операции для работы с дробями (операции +, -, *, /).
'''

class Drob:
    __chislitel: float
    __znamenatel: float

    def __init__(self, chislitel, znamenatel):
            self.__chislitel = chislitel
            self.__znamenatel = znamenatel

    @property
    def chislitel(self): return self.__chislitel

    @property
    def znamenatel(self): return self.__znamenatel

    @chislitel.setter
    def chislitel(self, chislitel): self.__chislitel = chislitel

    @znamenatel.setter
    def znamenatel(self, znamenatel): self.__znamenatel = znamenatel

    def __str__(self):
        return f'{self.chislitel} \\ {self.znamenatel}'

    def input(self):
        self.chislitel = input('Enter chislitel: ')
        self.znamenatel = input('Enter znamenatel: ')

    def __add__(self, other):
        if self.znamenatel != 0 and other.znamenatel != 0:
            if self.znamenatel == other.znamenatel:
                return (self.chislitel + other.chislitel) / self.znamenatel
            else:
                i = min(self.znamenatel, other.znamenatel)
                while True:
                    if i % self.znamenatel == 0 and i % other.znamenatel == 0:
                        break
                    i += 1
                return ((self.chislitel * (i / self.znamenatel)) + (other.chislitel * (i / other.znamenatel))) / i
        else:
            print('Знаменатель не должен быть равен нулю!')

    def __sub__(self, other):
        if self.znamenatel != 0 and other.znamenatel != 0:
            if self.znamenatel == other.znamenatel:
                return (self.chislitel - other.chislitel) / self.znamenatel
            else:
                i = min(self.znamenatel, other.znamenatel)
                while True:
                    if i % self.znamenatel == 0 and i % other.znamenatel == 0:
                        break
                    i += 1
                return ((self.chislitel * (i / self.znamenatel)) - (other.chislitel * (i / other.znamenatel))) / i
        else:
            print('Знаменатель не должен быть равен нулю!')

    def __mul__(self, other):
        if self.znamenatel != 0 and other.znamenatel != 0:
            return (self.chislitel * other.chislitel) / (self.znamenatel * other.znamenatel)
        else:
            print('Знаменатель не должен быть равен нулю!')

    def __truediv__(self, other):
        if self.znamenatel != 0 and other.znamenatel != 0:
            return (self.chislitel * other.znamenatel) / (self.znamenatel * other.chislitel)
        else:
            print('Знаменатель не должен быть равен нулю!')