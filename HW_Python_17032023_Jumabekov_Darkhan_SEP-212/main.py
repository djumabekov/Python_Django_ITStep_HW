from Blender import Blender
from Circle import Circle
from CoffeeMachine import CoffeeMachine
from Ellipse import Ellipse
from MeatGrinder import MeatGrinder
from Rectangle import Rectangle
from Shape import Shape
from Square import Square

if __name__ == '__main__':
    # Задание 1
    # Coffee Machine
    coffee_machine = CoffeeMachine("Coffee Machine", ['milk', 'sugar', 'coffee'], 'coffee')
    coffee_machine.turn_on()
    coffee_machine.get_output_product()
    coffee_machine.turn_off()

    print()
    # Blender
    blender = Blender("Blender", ['banana', 'kiwi', 'milk', 'icecream'], 'cocktail')
    blender.turn_on()
    blender.get_output_product()
    blender.turn_off()

    print()
    # MeatGrinder
    meatGrinder = MeatGrinder("MeatGrinder", ['meat', 'onion', 'garlic', 'pepper'], 'minced meat')
    meatGrinder.turn_on()
    meatGrinder.get_output_product()
    meatGrinder.turn_off()

    # Задание 2

    shapes_list = [
        Square('Square', 8, 4, 4),
        Rectangle('Rectangle', 12, 4, 5, 5),
        Circle('Circle', 8, 3, 3),
        Ellipse('Ellipse', 4, 9, 2, 2)
    ]

    for shape in shapes_list:
        shape.save('shapes.txt')
        print(f'{shape.show()} saved')

    shapes_list = Shape.load('shapes.txt')

    print(*shapes_list)



