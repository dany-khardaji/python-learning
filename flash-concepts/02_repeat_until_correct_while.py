password = "Josh"

while True:
    password_input = input("Enter password: ")

    if password_input == password:
        print("Correct!")
        break
    else:
        print("Wrong!")