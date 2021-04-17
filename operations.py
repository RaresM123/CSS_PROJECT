def add_negatives_numbers(first_number, second_number):
    result = []
    first_number = first_number[1:]
    second_number = second_number[1:]
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
        print(i)
        if result[i] > 10:
            result[i-1] = int(result[i]/10) + result[i-1]
            result[i] = int(result[i] % 10)
    if result[0] > 10:
        a = result[0] % 10
        b = int(result[0]/10)
        result[0] = a
        result.insert(0, b)
    result.insert(0, '-')
    print(result)
    return ''.join([str(item) for item in result])


def add_negative_positive_numbers(first_number, second_number):
    pass


def add_positive_numbers(first_number, second_number):

    result = []
    first_number = first_number[1:]
    second_number = second_number[1:]
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
        if result[i] > 10:
            result[i-1] = int(result[i]/10) + result[i-1]
            result[i] = int(result[i] % 10)
    if result[0] > 10:
        a = result[0] % 10
        b = int(result[0]/10)
        result[0] = a
        result.insert(0, b)
    result.insert(0, '+')
    print(result)
    return ''.join([str(item) for item in result])


def add_numbers(first_number, second_number):

    if first_number[0] == '-' and second_number[0] == '-':
        result = add_negatives_numbers(first_number, second_number)
    elif (first_number[0] == '-' and second_number[0] == '+') or (first_number[0] == '+' and second_number[0] == '-'):
        result = add_negative_positive_numbers(first_number, second_number)
    elif first_number[0] == '+' and second_number[0] == '+':
        result = add_positive_numbers(first_number, second_number)

    return result


def difference_positive_numbers(first_number, second_number):

    result = []
    first_number = first_number[1:]
    second_number = second_number[1:]

    _sign = '+'
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

    while len(second_number):
        last_digit_b = int(second_number[len(second_number) - 1])
        result.insert(0, last_digit_b)
        second_number = second_number[:len(second_number) - 1]
        _sign = '-'

    i = 0
    while result[i] == 0:
        i = i + 1
    result = result[i:]
    _sign = '+' if result[0] > 0 else '-'


    print(result)
    result = ''.join([_sign] + [str(abs(item)) for item in result])

    print(result)


def difference_numbers(first_number, second_number):

    if first_number[0] == '-' and second_number[0] == '-':
        result = difference_positive_numbers(second_number, first_number)

    elif first_number[0] == '-' and second_number[0] == '+':
        result = add_negatives_numbers(first_number, second_number)
    elif first_number[0] == '+' and second_number[0] == '-':
        result = add_positive_numbers(first_number, second_number)
    elif first_number[0] == '+' and second_number[0] == '+':
        result = difference_positive_numbers(first_number, second_number)

    return result



x = ['+', 9, 9, 1, 9, 5, 7, 6]
y = ['+', 9, 9, 5, 7, 6, 4, 8]

print(add_numbers(x, y))
print(9919576 + 9957648)
print(-12 + 11)
x = '+1234'
y = '+23456'

z = '+341'
t = '+323'
difference_numbers(z, t)