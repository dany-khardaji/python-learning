test_score1 = int(input("Enter your first test score: "))
test_score2 = int(input("Enter your second test score: "))
test_score3 = int(input("Enter your third test score: "))

test_score_list = [test_score1, test_score2, test_score3]

average = sum(test_score_list) / len(test_score_list)       # Calculates the average of the test scores by summing them and dividing by the number of scores.

print(f"Average: {average:.2f}")                            # :.2f formats the average to 2 decimal places.

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# PROGRAM FLOW
# 1. Get 3 test scores from the user
# 2. Store the test scores in a list
# 3. Calculate the average score
# 4. Display the average score
# 5. Compare the average against grade ranges
# 6. Determine the corresponding letter grade
# 7. Display the final letter grade

# SCALABLE BEST VERSION
# def get_scores(count):
#     return [int(input(f"Enter score {i+1}: ")) for i in range(count)]

# def calculate_grade(average):
#     if average >= 90: return "A"
#     elif average >= 80: return "B"
#     elif average >= 70: return "C"
#     elif average >= 60: return "D"
#     else: return "F"

# scores = get_scores(3)
# average = sum(scores) / len(scores)
# print(f"Average: {average:.2f} | Grade: {calculate_grade(average)}")