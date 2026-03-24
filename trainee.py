# 1. Capture the trainee's full name
trainee_name = input("Enter Trainee's Full Name: ")

# 2. Capture scores in specific assessment areas
# Using float to allow for decimal scores if necessary
syntax_score = float(input("Enter score for Python Syntax: "))
problem_solving_score = float(input("Enter score for Problem Solving: "))
mini_project_score = float(input("Enter score for Mini Project: "))

# 3 & 4. Calculate Total and Average
total_score = syntax_score + problem_solving_score + mini_project_score
average_score = total_score / 3

# 5. Assign Performance Grade using Conditional Logic
if average_score >= 80:
    grade = "Excellent"
elif average_score >= 70:
    grade = "Very Good"
elif average_score >= 60:
    grade = "Good"
elif average_score >= 50:
    grade = "Fair"
else:
    grade = "Needs Improvement"

# 6. Determine Completion Status
if average_score >= 50:
    status = "Competent"
else:
    status = "Not Yet Competent"

# 7. Display Professional Training Report
print("\n" + "="*30)
print("TRAINING PERFORMANCE REPORT")
print("="*30)
print(f"Trainee Name:      {trainee_name}")
print(f"Python Syntax:     {syntax_score}")
print(f"Problem Solving:   {problem_solving_score}")
print(f"Mini Project:      {mini_project_score}")
print("-" * 30)
print(f"Total Score:       {total_score:.2f}")
print(f"Average Score:     {average_score:.2f}")
print(f"Performance Grade: {grade}")
print(f"Completion Status: {status}")
print("="*30)