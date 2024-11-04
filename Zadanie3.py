def print_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


numbers = list(range(10))
print("Parzyste liczby:")
print_even_numbers(numbers)
