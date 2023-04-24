"""
Пользователь вводит с клавиатуры два числа,
выполните следующие операции:
1. Нужно показать все числа в указанном диапазоне.
2. Нужно показать все нечетные числа в указанном диапазоне.
3. Нужно показать все четные числа в указанном диапазоне.
4. Нужно показать все числа в указанном диапазоне в порядке убывания.
"""


def task_1():
    a = int(input('Введите число - начало диапазона: '))
    b = int(input('Введите число - конец диапазона: '))

    num = a + 1
    print('\n1. Нужно показать все числа в указанном диапазоне:')
    for i in range(abs(b - a - 1)):
        print(num + i, end=' ')

    print('\n2. Нужно показать все нечетные числа в указанном диапазоне.:')
    for i in range(abs(b - a - 1)):
        if i % 2:
            print(num + i, end=' ')

    print('\n3. Нужно показать все четные числа в указанном диапазоне.:')
    for i in range(abs(b - a - 1)):
        if not i % 2:
            print(num + i, end=' ')

    print('\n4. Нужно показать все числа в указанном диапазоне в порядке убывания.:')
    for i in reversed(range(abs(b - a - 1))):
        print(num + i, end=' ')


'''
5. Используя цикл for, выведите на экран для числа 2
его степени от 0 до 20.
Возведение в степень в Python обозначается как **.
'''


def task_2():
    for i in range(20):
        print(f'2^{i} = {2 ** i}')


if __name__ == '__main__':
    # task_1()
    task_2()