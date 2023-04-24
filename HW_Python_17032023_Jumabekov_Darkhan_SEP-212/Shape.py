'''
Задание 2
Создайте базовый класс Shape для рисования плоских фигур.
Определите методы:
Show() - вывод на экран информации о фигуре;
Save() - сохранение фигуры в файл;
Load() - считывание фигуры из файла.

Определите производные классы:
Square - квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
Rectangle - прямоугольник с заданными координатами верхнего левого угла и размерами;
Circle - окружность с заданными координатами центра и радиусом;
Ellipse - эллипс с заданными координатами верхнего угла.
Создайте список фигур, сохраните фигуры в файл, загрузите в другой список и отобразите информацию о каждой из фигур
'''

class Shape(object):
    __figure_name: str
    __startpoint_x: int
    __startpoint_y: int

    def __init__(self, figure_name, startpoint_x, startpoint_y):
        self.__figure_name = figure_name
        self.__startpoint_x = startpoint_x
        self.__startpoint_y = startpoint_y

    @property
    def figure_name(self): return self.__figure_name

    @property
    def startpoint_x(self): return self.__startpoint_x

    @property
    def startpoint_y(self): return self.__startpoint_y

    def show(self):
        return f'{self.figure_name}, x: {self.startpoint_x}, y: {self.startpoint_y}'

    def save(self, filename): ...

    @staticmethod
    def load(filename):
        shapes_list = open(filename, 'rt').read().split('end')
        return shapes_list
