from Shape import Shape


class Rectangle(Shape):

    __width: int
    __height: int

    def __init__(self, figure_name, height, width, startpoint_x, startpoint_y):
        super().__init__(figure_name, startpoint_x, startpoint_y)
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def save(self, filename):
        with open(filename, "a", encoding='utf-8') as file:
            file.write('\n' * self.startpoint_y)
            file.write(f'{super().show()}\n')
            for _ in range(self.width):
                file.write(' ' * self.startpoint_x)
                for _ in range(self.height):
                    file.write('* ')
                file.write('\n')
            file.write('end')
            file.close()
