## STRING SLICING (beginner friendly)
"""
Slicing lets you extract parts (substrings) from a string using the syntax:
	sequence[start:stop]
start is included, stop is excluded (Python uses half-open intervals).

Examples below show how to pick parts of the string.
"""

# Use a variable name other than the built-in `str`
s = "Faheem-Alam-Khan"
print("Original string:", s)
print()

# Basic slices:
print("s[2:5] -> characters at indexes 2,3,4 :", s[2:5])  # 'hee' (stop index 5 is not included)
print("To include index 5 as well, use s[2:6]:", s[2:6])      # 'heem'

# Slice a known region (Khan). Indexes: 'K' starts at 12 in this string
print("s[12:16] ->", s[12:16])

# You can use len(s) as the stop index to be explicit:
print("s[12:len(s)] ->", s[12:len(s)])

# If the stop is omitted, Python goes to the end of the string:
print("s[12:] ->", s[12:])

# If the start is omitted, Python starts from 0:
print("s[:6] ->", s[:6])  # first 6 characters

# Full copy of the string (useful to create a new string):
print("s[:] ->", s[:])

# Optional (slightly advanced) - step parameter: s[start:stop:step]
# Example: take every second character
print("s[::2] (every 2nd character) ->", s[::2])  # simple demo; you can skip this if new

# Short notes / gotchas:
# - The stop index is excluded. To include a character at index i, use stop=i+1.
# - Slicing never raises an error if indexes are out of range; it simply returns what exists.
# - To access a single character, use indexing (s[i]); slicing returns a new string.

# Suggested filename: string_slicing_examples.py
