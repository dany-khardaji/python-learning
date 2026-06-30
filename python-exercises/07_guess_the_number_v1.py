import random                               # importing the random module to generate a random number
secret_number = random.randint(1, 10)       # generates a random integer between 1 and 10 (inclusive) and stores it in the variable "secret_number"

guess = int(input("Guess the number: "))

if guess == secret_number:                 
    print("Correct!")

elif guess > secret_number:                 # if/elif/else checks conditions from top to bottom
    print("Too High!")                      # once a condition is true, Python runs that code and stops checking

else:                                       
    print("Too Low!")
    
