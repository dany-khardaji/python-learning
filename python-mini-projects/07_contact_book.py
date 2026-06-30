contacts = {}

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} added.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        else:
            print(f"Contact {name} not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    elif choice == "4":
        if len(contacts) == 0:
            print("No contacts saved.")
        else:
            for name, info in contacts.items():
                print(f"Name: {name}, Phone: {info["phone"]}, Email: {info["email"]}")

    elif choice == "5":
        print("Application terminated.")
        break
        

