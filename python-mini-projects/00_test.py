def get_scores(count):
    return [int(input(f"Enter score {i+1}: ")) for i in range(count)]

def calculate_grade(average):
    if average >= 90: return "A"
    elif average >= 80: return "B"
    elif average >= 70: return "C"
    elif average >= 60: return "D"
    else: return "F"

scores = get_scores(3)
average = sum(scores) / len(scores)
print(f"Average: {average:.2f} | Grade: {calculate_grade(average)}")