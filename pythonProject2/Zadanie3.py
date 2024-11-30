def is_even(number: int) -> bool:
    return number % 2 == 0


number = 4
result = is_even(number)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
