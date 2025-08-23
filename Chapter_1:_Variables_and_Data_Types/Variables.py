"""
VARIABLES IN PYTHON
-------------------
A variable is a name given to a memory location in a program. Variables are used to store data, just like in mathematics.
"""

# Example of variable assignment:
name = "Faheem Alam Khan"  # String: Always in double quotes. If quotes are removed, it will cause an error.

age = 17                   # Integer: Whole number value.

age2 = age                 # Assigning value of 'age' to 'age2'. Now, age2 is also 17.

price = 25.99              # Float: Decimal number value.

# Printing variable values:
print(name)                 # Prints the value stored in 'name'.
print(age)                  # Prints the value stored in 'age'.
print(age2)                 # Prints the value stored in 'age2'.
print(price)                # Prints the value stored in 'price'.

# You can print multiple variables at once, separated by commas:
print(name, age, price)

# The value of a variable is stored in a specific location in computer memory.
# If you change the value of a variable, only the value changes, not the variable name itself.

# You can also combine variables and strings in print statements:
print("My name is", name, "and my age is", age, "also I cost only", price)
# Note: Commas are important here. Without them, Python will show a syntax error.

# In mathematics, 'a = b' means a and b are equal.
# In Python, 'a = b' means the value of b is assigned to a. This is called the Assignment Operator.