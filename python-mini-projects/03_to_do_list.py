print("To-Do-List")
print("----------")
print("1. Add task")
print("2. View Tasks")
print("3. Quit")

task = 1
view = 2
quit = 3
task_list = []

print("----------")

while True:
    choose = int(input("Choose: "))
    if choose == task:
        add_task = input("Enter task: ")
        task_list.append(add_task)
    elif choose == view:
        print(f"My tasks: {task_list}")
    elif choose == quit:
        print("Application terminated.")
        break
    else:
        print("Invalid choice.")

# PROGRAM FLOW
# 1. Display the to-do list menu options
# 2. Create an empty task list
# 3. Ask the user to choose a menu option
# 4. Add a task if the user selects Add Task
# 5. Display all tasks if the user selects View Tasks
# 6. End the program if the user selects Quit
# 7. Show an error message for an invalid choice
# 8. Repeat until the user chooses to quit