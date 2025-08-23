
# STRING SLICING & NEGATIVE INDEXING - beginner friendly
"""
Slicing lets you extract substrings using the syntax: s[start:stop:step]
- start: index where slice begins (inclusive). Default = 0.
- stop: index where slice ends (exclusive). Default = len(s).
- step: how many characters to skip; default = 1.

Negative indexes count from the end: -1 is last char, -2 is second last, etc.
"""

# Use a safe variable name (don't shadow built-ins like `str`)
s = "APPLE"
print("Original string:", s)
print()

# Examples:
print("s[0:3] -> first three characters:", s[0:3])   # 'APP' (stop is excluded)
print("s[:3]  -> same as above (start default 0):", s[:3])
print("s[2:]  -> from index 2 to end:", s[2:])           # 'PLE'

# Negative indexing examples
print("Last character s[-1]:", s[-1])   # 'E'
print("Last three characters s[-3:]:", s[-3:])  # 'PLE'
print("All but last two s[:-2]:", s[:-2])  # 'APP'

# Step parameter examples
print("Every second character s[::2]:", s[::2])  # 'APE' (skip 1 each time)
print("Reverse string s[::-1]:", s[::-1])       # 'ELPPA' (useful trick)

# Common gotchas (beginner mistakes):
# - The 'stop' index is not included. s[0:3] returns indexes 0,1,2 only.
# - Accessing an index directly beyond the range (s[100]) raises IndexError, but slicing out-of-range
#   (s[0:100]) will simply return up to the end of the string without error.

# Practice examples you can try:
# - change s to a longer sentence and use different slices to see results
# - experiment with negative start/stop values to understand counting from the end
