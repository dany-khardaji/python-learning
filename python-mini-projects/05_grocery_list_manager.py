grocery_list = []

while True:
    print("======= Grocery List Manager =======")

    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    print("-------------------------------")

    choose = input("Choose an option: ")

    if choose == "1":
        item = input("Enter item: ")
        grocery_list.append(item)
        print("Item added!\n")

    elif choose == "2":
        item = input("Enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print("Item removed!\n")
        else:
            print("Item not found.\n")

    elif choose == "3":
        print("Current grocery list: ")
        if len(grocery_list) == 0:
            print("List is empty.")
        else:
            for item in grocery_list:
                print(item)
        print()

    elif choose == "4":
        print("Application terminated.")
        break

    else:
        print("Invalid Choice")

# PROGRAM FLOW
# 1. Display the grocery list menu options
# 2. Create an empty grocery list
# 3. Ask the user to choose a menu option
# 4. Add an item if the user selects Add Item
# 5. Remove an item if the user selects Remove Item
# 6. Check if the item exists before removing it
# 7. Display all items if the user selects View List
# 8. Show a message if the grocery list is empty
# 9. End the program if the user selects Exit
# 10. Show an error message for an invalid choice
# 11. Repeat until the user chooses to exit
    