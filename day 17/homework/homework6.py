def filter_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char in vowels])

print(filter_vowels("Hello World"))  # "eoo"
