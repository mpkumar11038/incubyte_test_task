def string_calculator(input_string):
    if not input_string:
        return 0
    numbers = input_string.split(',')
    total = sum([float(number) for number in numbers])
    return int(total)
