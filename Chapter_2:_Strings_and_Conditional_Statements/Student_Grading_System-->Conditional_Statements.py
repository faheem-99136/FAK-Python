# Student Grading System -> Conditional Statements
"""Grade students based on marks out of 100.

This script reads an integer mark, validates it, then assigns a grade
and prints a single, clear message.
"""

try:
    marks = int(input("Enter your marks (0-100): "))
except ValueError:
    print("Please enter a valid integer for marks.")
else:
    # Validate range first
    if marks < 0:
        print("Marks cannot be negative.")
    elif marks > 100:
        print("You can only enter up to 100, not above it.")
    else:
        # Calculate grade using descending checks (only lower bound needed)
        grade = None
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        elif marks >= 50:
            grade = 'E'
        elif marks >= 40:
            grade = 'F'
        else:
            grade = None  # failed

        # Print a single clear message
        if grade:
            print(f"You have received {grade} grade.")
        else:
            print("You have failed. Try again next year.")

# Notes for beginners:
# - We used try/except to handle non-integer input gracefully.
# - The checks use only the lower bound because previous conditions already
#   excluded higher values (e.g., if marks >= 90 is false, we know marks < 90).
# - Suggestion: you can store the grade in a variable (as done) and print once
#   at the end. This makes it easier to change output formatting later.

