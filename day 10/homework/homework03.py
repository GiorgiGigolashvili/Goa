correct_password = "gio123"
user_password = input("Enter your password: ")
while user_password != correct_password:
    print("Incorrect password. Try again.") 
    user_password = input("Enter your password: ")   

print("Correct password. You have successfully logged in.") 