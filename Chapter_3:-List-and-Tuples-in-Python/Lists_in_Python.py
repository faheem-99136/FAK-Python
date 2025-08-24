
# Lists in Python
"""
A list is a built-in data type that stores a collection of values. Lists can hold elements of different types (integer, float, string, etc.).
In other languages like C++, arrays must contain the same type, but Python lists can mix types.
"""

# Example: List of marks of students
stdnt1 = 94.4
stdnt2 = 87.5
stdnt3 = 95.2
stdnt4 = 66.4
stdnt5 = 45.1
# The above method is tedious; using a list is easier:
marks = [94.4, 87.5, 95.22, 66.4, 45.1]
print("Marks list:", marks)

# Check the type of 'marks'
print("Type of marks:", type(marks))  # <class 'list'>

# Get the length of the list
print("Number of students:", len(marks))

# Access elements by index
print("First mark:", marks[0])
print("Second mark:", marks[1])
print("Third mark:", marks[2])

# Lists can store mixed types
student_info = ["Faheem", 90.9, 428]  # name (str), marks (float), roll number (int)
print("Student info:", student_info)

"""
Lists and strings are similar (both are sequences), but:
- Strings are immutable (cannot be changed)
- Lists are mutable (can be changed)
"""

# Mutable: Can be changed
# Immutable: Cannot be changed

# Example: Strings are immutable
my_str = "hello"
print("First character of string:", my_str[0])  # Access is allowed
# my_str[0] = "y"  # Uncommenting this line will cause an error

# Example: Lists are mutable
print("Original name in student_info:", student_info[0])  # Access
student_info[0] = "Khan"  # Change value
print("Updated student_info:", student_info)
