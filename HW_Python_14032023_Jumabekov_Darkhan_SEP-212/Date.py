'''
Задание 2
Создайте класс Date, который будет содержать информацию о дате (день, месяц, год).
С помощью механизма перегрузки операторов, определите операцию разности двух дат
(результат в виде количества дней между датами), а также операцию увеличения даты на определенное количество дней.
'''

import datetime

class Date:
    __date: datetime.date

    def __init__(self, year, month, day):
        self.__date = datetime.date(year, month, day)

    def __add__(self, days: int):
        return self.__date + datetime.timedelta(days=days)

    def __sub__(self, other_date: datetime.date):
        delta = self.__date - other_date.__date
        return delta.days

    def __str__(self):
        return f'{self.__date}'

