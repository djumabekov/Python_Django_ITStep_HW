'''
Задание 1
Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте
класс CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере),
класс MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые для работы методы.
'''

class Device(object):
    __device_name: str
    __isTurnOn: bool
    def __init__(self, device_name):
        self.__device_name = device_name
        self.__isTurnOn = False

    @property
    def device_name(self): return self.__device_name

    @device_name.setter
    def device_name(self, device_name): self.__device_name = device_name

    def turn_on(self):
        if not self.__isTurnOn:
            self.__isTurnOn = True
            print(f'{self.device_name} is turn on')

    def turn_off(self):
        if self.__isTurnOn:
            self.__isTurnOn = False
            print(f'{self.device_name} is turn off')

    def get_output_product(self):
        if self.__isTurnOn:
            print(f'{self.device_name} get {self.output_product} with {self.input_ingredients}')
        else:
            print(f'Please turn on {self.device_name}')
