def sum_of_string(input_string):
    numbers = input_string.split(',')
    total = sum([int(number) for number in numbers])
    return total

