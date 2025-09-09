# Report Card Checker 🎓

A simple Python program that calculates a student's final grade based on their assignment, midterm, and final exam scores with user-defined weights.

## Features
- Input scores for assignments, midterm, and final exam
- Assign custom weights (must add up to 100%)
- Calculates total weighted score
- Outputs final letter grade (A-F)
- Displays a neat report card

## Example Run
```bash
Enter your name: Amani
Hello, Amani! Welcome to the report card generator.

Enter the subject: Math
Enter the assignments score (out of 100): 92
Enter the midterm score (out of 100): 85
Enter the final exam score (out of 100): 88

Now enter the weights for each section (as percentages).
Note: The weights should add up to 100%.
Enter the weight for assignments: 30
Enter the weight for midterm: 30
Enter the weight for final exam: 40

Total Score: 88.90

--- Report Card ---
Student: Amani
Subject: Math
Assignments (weighted): 27.60
Midterm (weighted): 25.50
Final Exam (weighted): 35.60
Total Score: 88.90
Grade: B
-------------------
Thank you for using the report card generator!
