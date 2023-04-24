from Rectangle import Rectangle
from Shape import Shape


class Ellipse(Rectangle):

    __width: int
    __height: int

    def __init__(self, figure_name, height, width, startpoint_x, startpoint_y):
        super().__init__(figure_name, height, width, startpoint_x, startpoint_y)

    def save(self, filename):
        with open(filename, "a", encoding='utf-8') as file:
            file.write('\n' * self.startpoint_y)
            file.write(f'{super().show()}\n')
            for y in range(-self.height, self.height + 1):
                file.write(' ' * self.startpoint_x)
                for x in range(-self.width, self.width + 1):
                    file.write(
                        ' * ' if x * x * self.height * self.height + y * y * self.width * self.width <= self.height * self.height * self.width * self.width else '   ')
                file.write('\n')
            file.write('end')
            file.close()
