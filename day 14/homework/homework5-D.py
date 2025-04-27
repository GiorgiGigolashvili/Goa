numbers = [2, 2, 9, 2, 2]
sorted_numbers = sorted(numbers)
for num in sorted_numbers:
    if sorted_numbers.count(num) == 1:
        unique_number = num
        break

print(f"განსხვავებული ელემენტია: {unique_number}")