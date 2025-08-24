"""
=================
Tuples in Python
=================
A tuple is a built-in data type that lets us create immutable sequences of values.
Just like strings, tuples are immutable (cannot be changed), while lists are mutable (can be changed).
"""

# Tuples use parentheses () instead of square brackets []
my_tuple = (2, 1, 4, 8, 7, 5, 3, 6, 9)

# Print the type of the tuple
print("Type of my_tuple:", type(my_tuple))

# Access elements by index
print("Element at index 0:", my_tuple[0])
print("Element at index 1:", my_tuple[1])
print("Element at index 2:", my_tuple[2])

# Tuples are immutable: the following operation is not allowed
# my_tuple[0] = 5  # Uncommenting this line will cause an error

# Tuples with a single value
tup = (1,)      # Comma is necessary for single-value tuple
tup1 = (1)      # Without comma, this is just an integer
tup2 = (1.0)    # Without comma, this is a float
tup3 = ("String") # Without comma, this is a string

print("Type of tup:", type(tup))    # tuple
print("Type of tup1:", type(tup1))  # int
print("Type of tup2:", type(tup2))  # float
print("Type of tup3:", type(tup3))  # str

# For multi-element tuples, the comma at the end is optional