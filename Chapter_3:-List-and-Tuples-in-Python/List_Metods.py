
# List Methods in Python
"""
List methods are special functions that work only with lists (not with strings or other types).
Below are some common list methods with examples and explanations.
"""

# Example lists
numbers = [85, 94, 76, 63, 48]
fruits = ["banana", "Litchi", "Apple"]
nums = [1, 2, 3, 1, 2, 3]

# a) append()
# Adds an element to the end of the list
numbers.append(50)  # Adds 50 at the end
print("After append:", numbers)

# b) sort()
# Sorts the list in ascending order (numbers or alphabetically)
numbers.sort()
print("Sorted numbers:", numbers)
fruits.sort()
print("Sorted fruits:", fruits)

# c) sort(reverse=True)
# Sorts the list in descending order
numbers.sort(reverse=True)
fruits.sort(reverse=True)
print("Descending numbers:", numbers)
print("Descending fruits:", fruits)

# d) reverse()
# Reverses the order of the list (does not sort)
numbers.reverse()
print("Reversed numbers:", numbers)
fruits.reverse()
print("Reversed fruits:", fruits)

# e) insert(index, value)
# Inserts a value at a specific index
numbers.insert(1, 5)  # Inserts 5 at index 1
print("After insert at index 1:", numbers)

# f) remove(value)
# Removes the first occurrence of the value
nums.remove(1)  # Removes the first 1
print("After remove 1:", nums)

# g) pop(index)
# Removes and returns the element at the given index
removed = nums.pop(3)  # Removes the element at index 3
print(f"After pop at index 3 (removed {removed}):", nums)