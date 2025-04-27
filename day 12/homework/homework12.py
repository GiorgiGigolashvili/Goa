age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"

if age == 14 and not is_student:
    print("You are 14 years old and not a student.")
else:
    print("Conditions do not match.")