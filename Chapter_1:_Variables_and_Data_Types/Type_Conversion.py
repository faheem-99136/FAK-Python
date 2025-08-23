# TYPE CONVERSION IN PYTHON
# ------------------------
# Type conversion is the process of converting one data type into another.
# There are two types in Python:
# (a) Type Conversion (automatic)
# (b) Type Casting (manual)

# Type Conversion: Done automatically by the interpreter
# Example: Adding an integer and a float results in a float

a = 2
b = 4.25
sum = a + b  # 'a' (int) + 'b' (float) gives a float result
print(sum)   # Output: 6.25

# Type Casting: Done manually by the programmer
# Example: Converting a string to an integer before addition

c = "3"
d = 4.26
#sam = c + d  # This would give an error because you can't add a string and a float

c = int("3")  # Convert string '3' to integer 3
sam = c + d   # Now addition works
print(sam)    # Output: 7.26

# You can also convert float to string

e = 3.14
# Convert float to string
e = str(e)
print(type(e))  # Output: <class 'str'>

# Use type() to check the type of any variable
# Type conversion and casting help you work with different data types in your programs!