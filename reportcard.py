name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the report card generator.\n")

subject = input("Enter the subject: ")

# Raw scores
assignments_score = float(input("Enter the assignments score (out of 100): "))
midterm_score = float(input("Enter the midterm score (out of 100): "))
final_exam_score = float(input("Enter the final exam score (out of 100): "))

# Weights
print("\nNow enter the weights for each section (as percentages).")
print("Note: The weights should add up to 100%.")
assignments_weight = float(input("Enter the weight for assignments: "))
midterm_weight = float(input("Enter the weight for midterm: "))
final_exam_weight = float(input("Enter the weight for final exam: "))

if (assignments_weight + midterm_weight + final_exam_weight) != 100:
    print("Error: The weights do not add up to 100%. Please restart the program and enter valid weights.")
    exit()

# Weighted scores
assignments_score = (assignments_score * assignments_weight) / 100
midterm_score = (midterm_score * midterm_weight) / 100
final_exam_score = (final_exam_score * final_exam_weight) / 100

# Total
total_score = assignments_score + midterm_score + final_exam_score
print(f"\nTotal Score: {total_score:.2f}")

# Letter grade
if total_score >= 90:
    grade = 'A'
elif total_score >= 80:
    grade = 'B'
elif total_score >= 70:
    grade = 'C'
elif total_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Report
print("\n--- Report Card ---")
print(f"Student: {name}")
print(f"Subject: {subject}")
print(f"Assignments (weighted): {assignments_score:.2f}")
print(f"Midterm (weighted): {midterm_score:.2f}")
print(f"Final Exam (weighted): {final_exam_score:.2f}")
print(f"Total Score: {total_score:.2f}")
print(f"Grade: {grade}")
print("-------------------")
print("Thank you for using the report card generator!")
