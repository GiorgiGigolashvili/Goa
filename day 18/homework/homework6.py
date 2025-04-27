fruits = ['apple', 'banana', 'cherry', 'grape', 'orange']
index = int(input("შეიყვანეთ ინდექსი: "))
if 0 <= index < len(fruits):
    fruits.pop(index)
    print("სიის საბოლოო ვერსია:", fruits)
else:
    print("ინდექსი არასწორია.")
