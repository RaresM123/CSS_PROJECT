from .operations import Operations


class BigNumber:

    def __init__(self, number):
        self.number = number
        self.operations = Operations()

    def __add__(self, o):
        return BigNumber(self.operations.add_numbers(self.number, o.number))

    def __sub__(self, o):
        return BigNumber(self.operations.difference_numbers(self.number, o.number))

    def __mul__(self, o):
        return BigNumber(self.operations.multiply_numbers(self.number, o.number))

    def __truediv__(self, o):
        return BigNumber(self.operations.divide_numbers(self.number, o.number))

    def __xor__(self, o):
        return BigNumber(self.operations.power_numbers(self.number, o.number))

    def __invert__(self):
        return BigNumber(self.operations.sqrt_numbers(self.number))

    def __repr__(self):
        return self.number


