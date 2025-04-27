def negative_numbers(lst):
    return [x for x in lst if x < 0]

print(negative_numbers([1, -2, 3, -4, 5]))  # [-2, -4]
