def  is_prime(n):
    if n <= 1:
           return False
    for i in range(2, n):
          if n % i == 0:
                return False
          return True
number = int(input("sheiyvanet ricxvi:"))
if is_prime:
      print("The number is prime")
else:
      print("The number isnt prime")