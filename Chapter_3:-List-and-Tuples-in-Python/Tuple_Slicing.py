"""
==================
Slicing in Tuples
==================
Tuple slicing works just like slicing in strings and lists.
Syntax: tuple[start:end] (end index is not included)
"""

# Example tuple
my_tuple = (2, 1, 4, 8, 7, 5, 3, 6, 9)

# Slicing from index 0 to 2 (end index 3 is not included)
print("my_tuple[0:3] =>", my_tuple[0:3])  # Output: (2, 1, 4)