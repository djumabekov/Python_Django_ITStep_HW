
from Drob import Drob
from Date import Date

if __name__ == '__main__':

    # Задание 1
    # d1 = Drob(3, 15)
    # d2 = Drob(40, 18)
    # print(d1 + d2)
    # print(d1 - d2)
    # print(d1 * d2)
    # print(d1 / d2)

    # Задание 2
    date1 = Date(2017, 5, 12)
    date2 = Date(2017, 5, 6)
    days = 5
    print(f'увеличения даты {date1} на {days} дней: {date1 + days}')
    print(f'количество дней между датами {date1} и {date2}: {date1 - date2}')

