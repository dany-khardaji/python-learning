print("Welcome to the Number Guessing Game!")

import random
secret_number = random.randint(1, 100)
count = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    count += 1                                                     # Takes count, add 1, put it back into count.
    if guess > secret_number:                                        
        print("Too High!")
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("\nYou are correct!")
        print(f"You guesed it in {count} tries.")
        break
    
# PROGRAM FLOW
# 1. Display a welcome message to the user
# 2. Generate a random secret number
# 3. Ask the user to guess the number
# 4. Count each guess attempt
# 5. Compare the guess to the secret number
# 6. Tell the user if the guess is too high or too low
# 7. Repeat until the correct number is guessed
# 8. Display a success message
# 9. Display the total number of attempts