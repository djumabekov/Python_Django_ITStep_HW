import math

"""
7. Старинными русскими денежными единицами являются:
1 рубль = 100 копеек, 1 гривна = 10 копеек, 1 алтын = 3 копейки, 1 полушка = 0,25 копейки.
Имеется A копеек.
Разложите имеющуюся сумму в копейках на сумму из x рублей + y гривен + z алтынов + v полушек.
"""


def task_7():
    sum = int(input('Введите сумму в копейках: '))
    ruble = sum // 100
    grivna = (sum % 100) // 10
    altyn = (sum % 100) % 10 // 3
    polushka = int((sum % 100) % 10 % 3 // .25)
    print(f'{ruble} рублей, {grivna} гривен, {altyn} алтынов, {polushka} полушек')
    pass


'''
8. Стрелка прибора вращается с постоянной скоростью, совершая w оборотов в секунду 
(не обязательно стрелка прибора, может быть это волчок в игре «Что? Где? Когда?» и т.п.) 
Угол поворота стрелки в нулевой момент времени примем за 0. Каков будет угол поворота через t секунд?
'''


def task_8():
    w = float(input('Количество оборотов в сек: '))
    t = float(input('Количество секунд: '))
    deg = (w * t * 360) % 360
    print(f'угол поворота через {t} секунд = {deg}')
    pass


'''
9. Вы стоите на краю дороги и от вас до ближайшего фонарного столба x метров. 
Расстояние между столбами y метров. На каком расстоянии от вас находится n-й столб?
'''


def task_9():
    x = float(input('Введите растояние до ближайшего фонарного столба: '))
    y = float(input('Введите растояние между столбами: '))
    n = int(input('Введите номер столба: '))
    m = y * (n - 1) + x
    print(f'{n} столб находится от вас на расстоянии {m} метров')
    pass


'''
10. Та же ситуация, что и в предыдущей задаче. Длина вашего шага z метров. 
Мимо скольких столбов , сделав n шагов?
'''


def task_10():
    x = float(input('Введите растояние до ближайшего фонарного столба: '))
    y = float(input('Введите растояние между столбами: '))
    z = float(input('Введите длину вашего шага: '))
    n = int(input('Введите количество шагов: '))
    p = int((z * n - x) / y)
    print(f'Вы пройдете мимо {p} столбов сделав {n} шагов')
    pass


'''
11. x — вещественное число. Запишите выражение, позволяющее выделить его дробную часть.
'''


def task_11():
    x = float(input('Введите вещественное число: '))
    e = int(str(x).split('.')[1])
    print(f'Дробная часть числа {x}: {e} ')
    pass


'''
12. x — вещественное число. Запишите выражение, которое округлит его до сотых долей 
(останется только два знака после запятой).
'''


def task_12():
    x = float(input('Введите вещественное число: '))
    print(f'Число {x} два знака после запятой: {round(x, 2)}')
    pass


'''
13. От бревна длиной L отпиливают куски длиной x. 
Сколько целых полноразмерных кусков максимально удастся отпилить?
'''


def task_13():
    l = float(input('Введите длину бревна: '))
    x = float(input('Введите длину куска: '))
    m = int(l // x)
    print(f'Максимально удастся отпилить {m} целых полноразмерных кусков')
    pass


'''
14. Бревно длиной L распилили в n местах. Какова средняя длина получившихся кусков?
'''


def task_14():
    l = float(input('Введите длину бревна: '))
    n = int(input('Введите количество распилов бревна: '))
    m = round(l / (n + 1), 2)
    print(f'Средняя длина получившихся кусков: {m}')
    pass


'''
15. Резиновое кольцо диаметром d разрезали в n местах. Какова средняя длина получившихся кусков?
'''


def task_15():
    d = float(input('Введите диаметр кольца: '))
    n = int(input('Введите количество мест разреза: '))
    m = math.pi * d / n
    print(f'Средняя длина получившихся кусков: {m}')
    pass


if __name__ == '__main__':
    task_7()
    # task_8()
    # task_9()
    # task_10()
    # task_11()
    # task_13()
    # task_14()
    # task_15()
