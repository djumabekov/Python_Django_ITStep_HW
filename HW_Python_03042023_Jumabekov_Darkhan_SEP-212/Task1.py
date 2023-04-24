'''
Задание 1.
Напишите программу, в котором пользователь вводит в текстовое поле
предложение, и при нажатии на кнопку во втором появляется то же предложение
наоборот.
Входные данные: На улице очень жаркая погода
Вывод: адогоп яакраж ьнечо ецилу аН
'''

from tkinter import *

root = Tk()

input1 = Entry(root, width=100)
output1 = Entry(root, width=100)

def strReverse():
    output1.insert(0, input1.get()[::-1])

button1 = Button(root, text="Перевернуть строку", command=strReverse)

input1.pack()
button1.pack()
output1.pack()

root.mainloop()