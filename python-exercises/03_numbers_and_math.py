number = int(input("Enter first number: "))       # Used input() function to get user input and converted it to an integer using int() function, then stored it under variable "number"
number2 = int(input("Enter second number: "))  

addition = number + number2                  # Added the two numbers together
subtraction = number - number2               # Subtracted the second number from the first
multiplication = number * number2            # Multiplied the two numbers together
division = number / number2                  # Divided the two numbers together

print()                                      # Adds a blank line for better readability of output
print(f"Addition: {addition}")               # Used f-string to print the result of addition
print(f"Subtraction: {subtraction}")         # Used f-string to print the result of subtraction
print(f"Multiplication: {multiplication}")   # Used f-string to print the result of multiplication
print(f"Division: {division}")               # Used f-string to print the result of division