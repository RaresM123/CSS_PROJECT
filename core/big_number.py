from .operations import Operations
from math import sqrt


def assert_preconditions(number):

    assert number.count('-') == 0, "the number is negative"
    assert number.isnumeric() is True or number == "0", "the number is not numeric"
    assert number.startswith("0") or number != "0", "The number can't start with 0"


def assert_invariant(number, result):

    assert type(number) == str, "different type for number"
    assert type(result) == BigNumber, "different type for result"
    assert number is not None, "None input"
    assert result is not None, "None result"


def assert_postconditions(result, operation, number_1, number_2):

    if operation == '/':
        assert str(eval(number_1 + "//" + number_2)) == result.number, "different result"
    elif operation == "^":
        assert str(eval("pow(" + number_1 + ',' + number_2 + ")")) == result.number, "different result"
    elif operation == "~":
        assert str(int(eval("sqrt(" + number_1 + ")"))) == result.number, "different result"
    else:
        assert str(eval(number_1 + operation + number_2)) == result.number, "different result"


class BigNumber:

    def __init__(self, number):
        assert_preconditions(number)
        self.number = number
        self.operations = Operations()

    def __add__(self, o):
        assert_preconditions(number=o.number)
        result = BigNumber(self.operations.add_numbers(self.number, o.number))
        assert_invariant(self.number, result)
        assert_invariant(o.number, result)
        assert_postconditions(result, '+', self.number, o.number)
        return result

    def __sub__(self, o):
        assert_preconditions(number=o.number)
        result = BigNumber(self.operations.difference_numbers(self.number, o.number))
        assert_invariant(self.number, result)
        assert_invariant(o.number, result)
        assert_postconditions(result, '/', self.number, o.number)
        return result

    def __mul__(self, o):
        assert_preconditions(number=o.number)
        result = BigNumber(self.operations.multiply_numbers(self.number, o.number))
        assert_invariant(self.number, result)
        assert_invariant(o.number, result)
        assert_postconditions(result, "*", self.number, o.number)
        return result

    def __truediv__(self, o):
        assert_preconditions(number=o.number)
        result = BigNumber(self.operations.divide_numbers(self.number, o.number))
        assert_invariant(self.number, result)
        assert_invariant(o.number, result)
        assert_postconditions(result, '/', self.number, o.number)
        return result

    def __xor__(self, o):
        assert_preconditions(number=o.number)
        result = BigNumber(self.operations.power_numbers(self.number, o.number))
        assert_invariant(self.number, result)
        assert_invariant(o.number, result)
        assert_postconditions(result, '^', self.number, o.number)
        return result

    def __invert__(self):
        assert_preconditions(self.number)
        result = BigNumber(self.operations.sqrt_numbers(self.number))
        assert_invariant(self.number, result)
        assert_postconditions(result, '~', self.number, None)
        return result

    def __repr__(self):
        return self.number


# x = BigNumber('3')
#
# print(x / BigNumber("2"))
#
# y = BigNumber("16")
# print((~y).number)
# number = "a123"
# print(number.startswith("0") is True and len(number) == 1)