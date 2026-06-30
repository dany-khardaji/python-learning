age = int(input("Enter your age: "))        # Get user input and convert it to an integer
print()
print(f"You are {age} years old.")          # Print the age entered by the user using f-string format

if age >= 18:                               # Check if the age is 18 or greater, if true, print the following
    print("You are an adult.")
else:                                       # If the age is less than 18, print the following
    print("You are a minor.")