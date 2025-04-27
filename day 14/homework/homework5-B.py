names = []
for _ in range(5):
    name = input("შეიყვანეთ სახელი: ")
    names.append(name)
for name in names:
    if len(name) > 5:
        print(f"{name} შედგება 5-ზე მეტი ასოსგან.")