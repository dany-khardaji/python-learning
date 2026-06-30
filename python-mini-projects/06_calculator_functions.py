def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: can't divide by zero"
    return a / b


while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")    
    print("4. Divide")
    print("5. Quit")

    choose_option = input("Choose an option: ")

    if choose_option == "5":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choose_option == "1":
        print("Result:", add(num1, num2))
    elif choose_option == "2":
        print("Result:", subtract(num1, num2))
    elif choose_option == "3":
        print("Result:", multiply(num1, num2))
    elif choose_option == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid option, try again!")