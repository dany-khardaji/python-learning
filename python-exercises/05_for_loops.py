name = input("Enter your name: ")   # get user input and store it in the variable "name"  

for _ in range(5):                  # range(5) generates: 0, 1, 2, 3, 4, _ takes each value one at a time, the code inside the loop runs once for each value                                   
    print(f"Hello {name}!")         # uses f-string with variable "name" to print a greeting