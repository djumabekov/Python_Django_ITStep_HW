from Shape import Shape


class Circle(Shape):

    __radius: int

    def __init__(self, figure_name, radius, startpoint_x, startpoint_y):
        super().__init__(figure_name, startpoint_x, startpoint_y)
        self.__radius = radius

    @property
    def radius(self): return self.__radius

    def save(self, filename):
        with open(filename, "a", encoding='utf-8') as file:
            file.write('\n' * self.startpoint_y)
            file.write(f'{super().show()}\n')
            for y in range(-self.radius, self.radius+1):
                file.write(' ' * self.startpoint_x)
                for x in range(-self.radius, self.radius+1):
                    file.write(' * ' if x * x + y * y <= self.radius * self.radius else '   ')
                file.write('\n')
            file.write('end')
            file.close()



