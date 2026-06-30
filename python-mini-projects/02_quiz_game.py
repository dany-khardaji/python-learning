print("Welcome to my quiz game!\n")

color_answer = ["blue", "Blue"]
math_answer = 4
count = 0

while True:

    math_question = int(input("What is 2 + 2? "))

    if math_question == math_answer:
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    color_question = input("What is the color of the sky? ")

    if color_question in color_answer:
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    break
        
print(f"Final Score: {count}/2")

# PROGRAM FLOW
# 1. Display a welcome message to the user
# 2. Ask the first quiz question
# 3. Check if the first answer is correct
# 4. Increase the score for a correct answer
# 5. Repeat until the first question is answered correctly
# 6. Ask the second quiz question
# 7. Check if the second answer is correct
# 8. Increase the score for a correct answer
# 9. Repeat until the second question is answered correctly
# 10. Display the final score