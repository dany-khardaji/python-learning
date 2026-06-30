gradebook = {}

while True:
    print("1. Add student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Quit")

    choose = input("Choose an option: ")

    if choose == "1":
        name = input("Enter student name: ")
        math = input("Enter math grade: ")
        science = input("Enter science grade: ")
        history = input("Enter history: ")
        gradebook[name] = {
            "Math grade": math,
            "Science grade": science,
            "History grade": history
        }
        print(f"Student {name} added!")

    elif choose == "2":
        name = input("Enter name to search: ")
        if name in gradebook:
            print(
                f"Name: {name}, "
                f"Math grade: {gradebook[name]['Math grade']}, "
                f"Science grade: {gradebook[name]['Science grade']}, "
                f"History grade: {gradebook[name]['History grade']}"
            )   
        else:
            print("Invalid Entry")

    elif choose == "3":
        name = input("Enter name to delete: ")
        if name in gradebook:
            del gradebook[name]
            print (f"{name} has been removed.")
        else:
            print("Invalid entry.")
        
    elif choose == "4":
        if len(gradebook) == 0:
            print ("Gradebook is empty.")
        else:
            for student in gradebook:
                print(f"Name: {student}")

    elif choose == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid entry.")