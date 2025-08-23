
# ===============================
# CONDITIONAL STATEMENTS IN PYTHON
# ===============================
# This file covers:
#   - if, elif, else structure
#   - Real-life examples
#   - Indentation rules
#   - Multiple examples for practice
# ===============================

# --- Definition ---
# Conditional statements allow you to execute code only if certain conditions are met.
# Syntax:
# if condition:
#     statement(s)
# elif condition:
#     statement(s)
# else:
#     statement(s)

# --- Real-life examples ---
# 1. Voting or driving eligibility (age >= 18)
# 2. Student grading system (percentage >= 90: A1+, 80-89: A1, etc.)
# 3. Comparing numbers

# --- Example 1: Age check ---
age = int(input("Enter your age: "))  # User inputs their age

if age >= 18:
     print("You are eligible to vote & apply for a gun licence.")
     print("You can drive too!")
elif age > 0 and age < 18:
     print("You are not eligible.")
else:
     print("Invalid age entered.")

# --- Example 2: Student Grading System ---
percentage = float(input("Enter your percentage: "))
if percentage >= 90:
     print("Grade: A1+")
elif percentage >= 80:
     print("Grade: A1")
elif percentage >= 70:
     print("Grade: A")
elif percentage >= 60:
     print("Grade: B")
elif percentage >= 50:
     print("Grade: C")
else:
     print("Grade: F (Fail)")

# --- Example 3: Number Comparison ---
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
     print(f"{num1} is greater than {num2}")
elif num1 < num2:
     print(f"{num2} is greater than {num1}")
else:
     print("Both numbers are equal.")

# --- Notes ---
# - Indentation (spaces/tabs) is required after ':' in Python.
# - You can have multiple elif branches.
# - else is optional and runs if no previous condition is true.