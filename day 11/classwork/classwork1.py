total_sum = 0

for i in range(10):
    number = int(input("მომხმარებლისგან რიცხვის შეყვანა: "))
    total_sum += number
    average = total_sum / 10

print(f"რიცხვების ჯამი: {total_sum}")
print(f"საშუალო არითმეტიკული: {average}")