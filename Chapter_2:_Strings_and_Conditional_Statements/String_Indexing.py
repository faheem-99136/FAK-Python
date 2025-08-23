
# INDEXING - beginner friendly examples
"""
Indexing: each character in a Python string has an index (a position number).
Indexes start at 0. Use square brackets to access a character by index.

Example positions (0-based):
	F  A  H  E  E  M  -  A  L  A  M   ' '   K  H  A  N
	0  1  2  3  4  5  6  7  8  9  10  11  12 13 14 15

Note: Strings are immutable — you cannot assign to s[4] directly.
To change a character, create a new string using slicing and concatenation.
"""

# Use a variable name other than `str` to avoid shadowing the built-in type
s = "FAHEEM-ALAM KHAN"
print("String:", s)
print()

# Access by positive index (0-based)
ch1 = s[3]        # 4th character (index 3)
print("Character at index 3:", ch1)  # Output: 'E'

# Access a character that is a space - printing directly looks empty
ch2 = s[11]
print("Character at index 11 (repr to show space):", repr(ch2))  # Output: ' ' (a space)
print("Is index 11 a space?", ch2 == ' ')

# Negative indexing: -1 is last character, -2 is second last, etc.
print("Last character (s[-1]):", s[-1])   # 'N'
print("Second last (s[-2]):", s[-2])     # 'A'

# Length of the string
print("Length of string (len(s)):", len(s))  # 16

# Slicing: substring extraction using [start:stop] (stop is excluded)
print("First 6 characters (s[0:6]):", s[0:6])   # 'FAHEEM'
print("From index 7 to end (s[7:]):", s[7:])      # 'ALAM KHAN'

# Immutability: you cannot do s[4] = '@' — the following is INVALID and will raise an error
# s[4] = '@'  # Uncommenting this will raise TypeError: 'str' object does not support item assignment

# To replace a character, build a new string with slicing:
new_s = s[:4] + '@' + s[5:]
print("New string after replacing index 4 with '@':", new_s)

# Common gotchas:
# - Accessing an index outside range (e.g., s[100]) raises IndexError.
# - Indexing is case-sensitive: s[0] is 'F', not 'f'.

# Practice: try changing values and printing to see behavior, but avoid using variable name `str` in your code.