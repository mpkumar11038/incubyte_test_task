def string_calculator(input_string):
    numbers = input_string.split(',')
    total = sum([float(number) for number in numbers])
    return int(total)

