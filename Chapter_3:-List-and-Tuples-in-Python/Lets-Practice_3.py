
# Lets Practice:
"""
Write a program to count the number of students with a specific grade in the following tuple:
       ("C", "D", "A", "A", "B", "B", "A")
"""

# Tuple containing grades of students
grades = ("C", "D", "A", "A", "B", "B", "A")

# Display the grades
print("Student grades:", grades)

# Ask the user which grade to count
grade_to_count = input("Enter the grade you want to count (e.g., A, B, C, D): ")

# Count and display the number of times the grade appears
count = grades.count(grade_to_count)
print(f"Grade '{grade_to_count}' occurs {count} times.")
