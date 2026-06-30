password = "python"

entered_password = input("Enter password: ")

while entered_password != password:                       
    print("Incorrect password. Try again.")               # keep asking for the password while it is wrong.
    entered_password = input("Enter password: ")          # 
