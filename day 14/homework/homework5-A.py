numbers = []
for _ in range(10):
    num = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)
for num in numbers:
    if num % 2 == 0:
        print(f"{num} არის ლუწი.")
    else:
        print(f"{num} არის კენტი.")