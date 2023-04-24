from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, figure_name, width, startpoint_x, startpoint_y):
        super().__init__(figure_name, width, width, startpoint_x, startpoint_y)
        self.__width = width





