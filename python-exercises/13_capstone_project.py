test_score_1 = int(input("Enter score one: "))
test_score_2 = int(input("Enter score two: "))
test_score_3 = int(input("Enter score three: "))

test_scores = [test_score_1, test_score_2, test_score_3]          # Creating a list called "test_scores" that contains the three test scores entered by the user   

print("These are your scores: ")
for test_score in test_scores:                               # For loop iterating through each score in the test_scores and printing it
    print(test_score)

average_score = sum(test_scores) / len(test_scores)               # Calculating the average score by summing all the scores in the test_scores and dividing by the number of scores (length of the list)

def display_result(average_score):                                # Defining a function called "display_result" that takes the average score as an argument and displays the average score and whether the user passed or failed based on the average score
    print(f"Average score: {average_score}")                    # Printing the average score using an f-string to format the output

    if average_score >= 60:                                       # If statement checking if the average score is greater than or equal to 60, which is the passing score
        print("You Passed!")
    else:
        print("You Failed!")

display_result(average_score)                                     # Call the function and send it the average score

