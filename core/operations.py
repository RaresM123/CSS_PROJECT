from math import sqrt


def assert_preconditions(number):

    assert number.count('-') == 0, "the number is negative"
    assert number.isnumeric() is True or number == "0", "the number is not numeric"
    assert (number[0] == '0' and len(number) == 1) or number[0] != '0', "The number can't start with 0"


def assert_invariant(first_number, second_number):
    if second_number == "sqrt":
        assert type(first_number) == str, "different type for first number"
        assert first_number is not None, "None first number"
    else:
        assert type(first_number) == str, "different type for first number"
        assert type(second_number) == str, "different type for second result"
        assert first_number is not None, "None first number"
        assert second_number is not None, "None second number"


def assert_postconditions(result, operation, number_1, number_2):

    if operation == '/':
        assert str(eval(number_1 + "//" + number_2)) == result, "different result"
    elif operation == "^":
        assert str(eval("pow(" + number_1 + ',' + number_2 + ")")) == result, "different result"
    elif operation == "~":
        assert str(int(eval("sqrt(" + number_1 + ")"))) == result, "different result"
    else:
        assert str(eval(number_1 + operation + number_2)) == result, "different result"


class Operations:

    def __add_positive_numbers(self, first_number, second_number):
        result = []
        while len(first_number) and len(second_number):

            last_digit_a = int(first_number[len(first_number)-1])
            last_digit_b = int(second_number[len(second_number)-1])
            result.insert(0, last_digit_a + last_digit_b)
            first_number = first_number[:len(first_number) - 1]
            second_number = second_number[:len(second_number) - 1]

        while len(first_number):
            last_digit_a = int(first_number[len(first_number)-1])
            result.insert(0, last_digit_a)
            first_number = first_number[:len(first_number) - 1]

        while len(second_number):
            last_digit_b = int(second_number[len(second_number) - 1])
            result.insert(0, last_digit_b)
            second_number = second_number[:len(second_number) - 1]

        for i in range(len(result) - 1, 0, -1):
            # print(i)
            if result[i] >= 10:
                result[i-1] = int(result[i]/10) + result[i-1]
                result[i] = int(result[i] % 10)
        if result[0] > 10:
            a = result[0] % 10
            b = int(result[0]/10)
            result[0] = a
            result.insert(0, b)
        # print(result)
        return ''.join([str(item) for item in result])

    def add_numbers(self, first_number, second_number):

        assert_invariant(first_number, second_number)
        assert_preconditions(first_number)
        assert_preconditions(second_number)
        result = self.__add_positive_numbers(first_number, second_number)
        assert_postconditions(result, "+", first_number, second_number)

        return result

    def __process_equal_len_numbers(self, result):
        for i in range(len(result) - 1, 0, -1):
            if result[i] < 0:
                result[i-1] = result[i-1] - 1
                result[i] = 10 + result[i]
        return result

    def __process_different_len_numbers(self, result):

        for i in range(len(result)-1, 0, -1):
            if result[i] < 0:
                result[i] = result[i] + 10
                result[i-1] = result[i-1] - 1
        return result

    def __difference_positive_numbers(self, first_number, second_number):
        if len(first_number) < len(second_number):
             raise ValueError("Negative result for difference for arguments "+first_number+", "+second_number)
        first_number_copy,second_number_copy=first_number,second_number
        result = []
        _equal_case = False
        _sign = '+'

        if len(first_number) == len(second_number):
            _equal_case = True

        while len(first_number) and len(second_number):

            last_digit_a = int(first_number[len(first_number)-1])
            last_digit_b = int(second_number[len(second_number)-1])
            result.insert(0, last_digit_a - last_digit_b)
            first_number = first_number[:len(first_number) - 1]
            second_number = second_number[:len(second_number) - 1]

        while len(first_number):
            last_digit_a = int(first_number[len(first_number)-1])
            result.insert(0, last_digit_a)
            first_number = first_number[:len(first_number) - 1]
            _sign = '+'

        while len(second_number):
            last_digit_b = int(second_number[len(second_number) - 1])
            result.insert(0, last_digit_b)
            second_number = second_number[:len(second_number) - 1]
            _sign = '-'

        if not any(result):
            return '0'
        i = 0

        while result[i] == 0:
            i = i + 1
        result = result[i:]
        if result[0] < 0:
            raise ValueError("Negative result for difference for arguments "+first_number_copy+", "+second_number_copy)
        if _equal_case:
            result = ''.join([str(item) for item in self.__process_equal_len_numbers(result)])
        else:
            result = ''.join([str(item) for item in self.__process_different_len_numbers(result)])

        i = 0
        while result[i] == '0':
            i = i + 1
        result = result[i:]

        return result

    def difference_numbers(self, first_number, second_number):

        assert_invariant(first_number, second_number)
        assert_preconditions(first_number)
        assert_preconditions(second_number)
        result = self.__difference_positive_numbers(first_number, second_number)
        assert_postconditions(result, "-", first_number, second_number)

        return result

    def __zeroPad(self, numberString, zeros, left = True):
        """Return the string with zeros added to the left or right."""
        for i in range(zeros):
            if left:
                numberString = '0' + numberString
            else:
                numberString = numberString + '0'
        return numberString

    def __karatsubaMultiplication(self, x ,y):
        """Multiply two integers using Karatsuba's algorithm."""
        #convert to strings for easy access to digits
        #base case for recursion

        if len(x) == 1 and len(y) == 1:
            return int(x) * int(y)
        if len(x) < len(y):
            x = self.__zeroPad(x, len(y) - len(x))
        elif len(y) < len(x):
            y = self.__zeroPad(y, len(x) - len(y))
        n = len(x)
        j = n//2
        #for odd digit integers
        if (n % 2) != 0:
            j += 1
        BZeroPadding = n - j
        AZeroPadding = BZeroPadding * 2
        a = x[:j]
        b = x[j:]
        c = y[:j]
        d = y[j:]
        #recursively calculate
        ac = self.__karatsubaMultiplication(a, c)
        bd = self.__karatsubaMultiplication(b, d)
        k = self.__karatsubaMultiplication(str(int(a) + int(b)), str(int(c) + int(d)))
        A = int(self.__zeroPad(str(ac), AZeroPadding, False))
        B = int(self.__zeroPad(str(k - ac - bd), BZeroPadding, False))
        return A + B + bd

    def multiply_numbers(self, first_number, second_number):

        assert_invariant(first_number, second_number)
        assert_preconditions(first_number)
        assert_preconditions(second_number)
        result = str(self.__karatsubaMultiplication(first_number, second_number))
        assert_postconditions(result, "*", first_number, second_number)

        return result

    def __compare_result(self,result, second_number):

        if len(result) < len(second_number):
            return False

        if len(result) == len(second_number):

            for i in range(len(result)):
                if int(result[i]) == int(second_number[i]):
                    continue
                if int(result[i]) > int(second_number[i]):
                    return True
                if int(result[i]) < int(second_number[i]):
                    return False
        return True

    def __divide_positive_numbers(self, first_number, second_number):

        if len(first_number) < len(second_number):
            return '0'

        result = self.difference_numbers(first_number, second_number)
        return_value = 1
        while self.__compare_result(result, second_number):
            return_value += 1
            result = self.difference_numbers(result, second_number)

        return str(return_value)

    def divide_numbers(self, first_number, second_number):

        assert_invariant(first_number, second_number)
        assert_preconditions(first_number)
        assert_preconditions(second_number)
        if first_number == '0' or second_number == '0':
            raise ValueError("Division by zero from numbers "+first_number+", "+second_number)

        result = self.__divide_positive_numbers(first_number, second_number)
        assert_invariant(first_number, second_number)
        assert_postconditions(result, "/", first_number, second_number)

        return result

    def power_numbers(self, first_number, second_number):

        assert_invariant(first_number, second_number)
        assert_preconditions(first_number)
        assert_preconditions(second_number)

        result = '1'
        for _ in range(int(second_number)):
            result = str(self.multiply_numbers(result, first_number))
        assert_postconditions(result, "^", first_number, second_number)

        return result

    def sqrt_numbers(self, first_number):

        assert_invariant(first_number, "sqrt")
        assert_preconditions(first_number)

        if first_number == '0' or first_number == '1':
            return first_number
        last_guess = self.divide_numbers(first_number, '2')
        while True:
            guess = self.divide_numbers(self.add_numbers(last_guess, self.divide_numbers(first_number, last_guess)), '2')
            if abs(int(guess) - int(last_guess)) <= 1:
                assert_postconditions(str(int(guess)), "~", first_number, None)
                return str(int(guess))
            last_guess = guess


if __name__ == '__main__':

    op = Operations()

    print(op.sqrt_numbers('4'))

    # print(op.add_numbers("1243", 5))

    # print(op.multiply_numbers("123", "-132"))

    # print(op.multiply_numbers("123", "asd"))

    # print(op.divide_numbers('123', '0'))

    # print(op.divide_numbers('123', '00'))

    # print(op.power_numbers(12, "2"))

