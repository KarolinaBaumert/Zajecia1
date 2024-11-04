def multiply_by_two_for(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


def multiply_by_two_comprehension(numbers):
    return [number * 2 for number in numbers]


numbers = [1, 2, 3, 4, 5]

print("Wersja z użyciem pętli for:")
print(multiply_by_two_for(numbers))

print("Wersja z użyciem listy składającej:")
print(multiply_by_two_comprehension(numbers))
