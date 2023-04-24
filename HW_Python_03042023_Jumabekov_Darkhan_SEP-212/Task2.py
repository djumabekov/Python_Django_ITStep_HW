'''
Задание 2.
Напишите простейший калькулятор, состоящий из двух текстовых полей,
куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". Результат
вычисления должен отображаться в метке. Если арифметическое действие
выполнить невозможно (например, если были введены буквы, а не числа), то в
метке должно появляться слово "ошибка".
'''

from tkinter import *

root = Tk()

first_num = Entry(root, width=20)
second_num = Entry(root, width=20)
operand = Label(root, width=10)
result = Label(root, width=30, text='0')

def calc(m):
    print("m ", m)
    try:
        res = 0
        match m:
            case '+':
                res = int(first_num.get()) + int(second_num.get())
            case '-':
                res = int(first_num.get()) - int(second_num.get())
            case '*':
                res = int(first_num.get()) * int(second_num.get())
            case '/':
                res = int(first_num.get()) / int(second_num.get())
            case _:
                res = 'ошибка'
        result['text'] = res
    except:
        result['text'] = 'ошибка'


plus = Button(root, text="+", width=10, command=lambda m="+": calc(m))
minus = Button(root, text="-", width=10, command=lambda m="-": calc(m))
mult = Button(root, text="*", width=10, command=lambda m="*": calc(m))
div = Button(root, text="/", width=10, command=lambda m="/": calc(m))

first_num.pack()
second_num.pack()
result.pack()
plus.pack()
minus.pack()
mult.pack()
div.pack()

root.mainloop()
