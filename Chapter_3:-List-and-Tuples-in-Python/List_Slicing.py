
# List Slicing in Python
"""
List slicing lets you extract parts of a list using indexes, just like string slicing.
Syntax: list[start:end] (end index is not included)
You can also use negative indexes.
"""

marks = [87, 64, 33, 95, 76]

# Slicing from index 1 to 3 (end index 4 is not included)
print("marks[1:4] =>", marks[1:4])  # [64, 33, 95]

# Slicing from start to index 3
print("marks[:4] =>", marks[:4])    # [87, 64, 33, 95]

# Slicing from index 1 to the end
print("marks[1:] =>", marks[1:])    # [64, 33, 95, 76]

# Slicing with negative indexes
print("marks[-3:-1] =>", marks[-3:-1])  # [33, 95]