from datetime import datetime


class Stadium:
    __name: str
    __date: datetime
    __country: str
    __city: str
    __capacity: int

    def __init__(self, *args, **kwargs):
        keys = ['name', 'date', 'country', 'city', 'capacity']
        for key in kwargs:
            try:
                idx = keys.index(str(key))
            except:
                idx = -1  # недействительный ключ, атрибут

            match idx:
                case 0:  # 'name'
                    self.name = kwargs[key]
                case 1:  # 'date'
                    self.date = kwargs[key]
                case 2:  # 'country'
                    self.country = kwargs[key]
                case 3:  # 'city'
                    self.city = kwargs[key]
                case 4:  # 'capacity'
                    self.capacity = kwargs[key]
                case _:  # default:
                    print('Неверный парамер ' + str(key))

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date

    @property
    def country(self):
        return self.__country

    @property
    def city(self):
        return self.__city

    @property
    def capacity(self):
        return self.__capacity

    @name.setter
    def name(self, name):
        self.__name = name

    @date.setter
    def date(self, date):
        self.__date = date

    @country.setter
    def country(self, country):
        self.__country = country

    @city.setter
    def city(self, city):
        self.__city = city

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity


    def __str__(self):
        return f'{self.name} \
           | {self.date} \
           | {self.country} \
           | {self.city} \
           | {self.capacity} '

    def input(self):
        self.name = input('Enter name: ')
        self.date = input('Enter date: ')
        self.country = input('Enter country: ')
        self.city = input('Enter city: ')
        self.capacity = input('Enter capacity: ')