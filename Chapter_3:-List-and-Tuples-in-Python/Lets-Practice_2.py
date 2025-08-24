
# Lets Practice:
"""
Write a program to check if a list contains a palindrome of elements.
Hint: use the copy() method.
"""

# A palindrome is a sequence that reads the same forwards and backwards.
# Example: ["m", "a", "a", "m"] is a palindrome, [1, 2, 3] is not.

List1 = ["m", "a", "a", "m", "p"]  # Change this to test other lists
List2 = [1, 2, 3]  # Example of a non-palindrome

# Make a copy of List1 so we don't modify the original
copy_list1 = List1.copy()
# Reverse the copy
copy_list1.reverse()

# Compare the reversed copy to the original
if copy_list1 == List1:
    print("Palindrome")
else:
    print("Not a palindrome")
