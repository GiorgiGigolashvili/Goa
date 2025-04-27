def positive_numbers(lst):
    return [x for x in lst if x > 0]

print(positive_numbers([1, -2, 3, -4, 5]))  # [1, 3, 5]
