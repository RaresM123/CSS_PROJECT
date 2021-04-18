from operations import *


class BigNumber:

    def __init__(self, number):
        self.number = number

    def __add__(self, o):
        return BigNumber(add_numbers(self.number, o.number))

    def __sub__(self, o):
        return BigNumber(difference_numbers(self.number, o.number))

    def __mul__(self, o):
        return BigNumber(multiply_numbers(self.number, o.number))

    def __floordiv__(self, o):
        return BigNumber(divide_numbers(self.number, o.number))

    def __xor__(self, o):
        return BigNumber(power_numbers(self.number, o.number))

    def __invert__(self):
        return BigNumber(sqrt_numbers(self.number))


y = BigNumber("16")
print((~y).number)
