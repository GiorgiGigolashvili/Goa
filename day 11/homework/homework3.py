def user_login():
    correct_username = "user123"
    correct_password = "pass123"

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login successful!")
            break
        else:
            print("Incorrect username or password. Please try again.")

user_login()