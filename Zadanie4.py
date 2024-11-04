def print_every_second_number(numbers):
    for i in range(1, len(numbers), 2):
        print(numbers[i])


numbers = list(range(10))
print_every_second_number(numbers)
