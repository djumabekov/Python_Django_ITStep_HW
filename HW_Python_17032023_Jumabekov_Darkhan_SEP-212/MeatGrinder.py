from Device import Device


class MeatGrinder(Device):
    __input_ingredients: list
    __output_product: str

    def __init__(self, device_name: str, input_ingredients: list, output_product: str):
        self.__input_ingredients = input_ingredients
        self.__output_product = output_product
        super().__init__(device_name)

    @property
    def output_product(self): return self.__output_product

    @property
    def input_ingredients(self): return self.__input_ingredients

    @output_product.setter
    def descr(self, output_product): self.__output_product = output_product

    @input_ingredients.setter
    def input_ingredients(self, input_ingredients): self.__input_ingredients = input_ingredients
