def merge_and_cube_lists(list1: list, list2: list) -> list:
    merged_list = list(set(list1 + list2))
    cubed_list = [x**3 for x in merged_list]
    return cubed_list

result = merge_and_cube_lists([1, 2, 3], [3, 4, 5])

print(result)
