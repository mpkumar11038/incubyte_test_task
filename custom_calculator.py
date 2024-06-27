def decorator_func(original_func):
    def wrapper(input_string):
        numbers = input_string.split(',')
        # # delimiter, nums = input_string.split('\n', 1)
        # # delimiter = delimiter[2:]
        # input_string = nums.replace(delimiter, ',')
        # input_string = input_string.replace('\n', ',').rstrip(',')
        # numbers = input_string.split(',')
        return original_func(numbers)
    return wrapper

@decorator_func
def string_calculator(input_string):
    print(input_string)
    negative_numbers = []
    if not input_string:
        return 0
    # elif input_string.startswith('//'):
    #     delimiter, nums = input_string.split('\n', 1)
    #     delimiter = delimiter[2:]
    #     input_string = nums.replace(delimiter, ',')
    # input_string = input_string.replace('\n', ',').rstrip(',')
    # numbers = input_string.split(',')
    numbers = input_string
    total = sum([float(number) for number in numbers])
    numbers = [negative_numbers.append(number) for number in numbers if float(number) < 0]
    if negative_numbers:
        negative_numbers_str = ', '.join(map(str, negative_numbers))
        raise ValueError(f"Negative numbers not allowed: {negative_numbers_str}")
    return int(total)




print(string_calculator("1,2,3,4,5"))