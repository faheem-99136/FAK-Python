
# INTRO TO STRINGS (beginner friendly)
"""
Strings store sequences of characters. You can use single quotes, double quotes,
or triple quotes to define strings in Python.
"""

# Examples using different quote styles
str1 = "This is a string (double quotes)"
str2 = 'This is also a string (single quotes)'
str3 = """This is a string using triple quotes.
Triple quotes are useful for multi-line strings and long text."""

# Why multiple quote styles?
# - If your string contains a single quote (apostrophe), use double quotes to avoid escaping.
example1 = "This is Faheem's laptop"  # safe: double quotes outside

# - If your string contains double quotes, use single quotes outside.
example2 = 'He said "Hello" to everyone'

# - Triple quotes allow multi-line strings without using \n manually
print(str3)

# Escape sequences (beginner):
# - \n starts a new line, \t is a tab, \\ is a single backslash, and \" or \\' escape quotes
escaped = "Line1\nLine2\t(Indented)"
print(escaped)

# Short notes:
# - Strings are immutable (can't change characters by assignment).
# - Use + to concatenate strings and len() to get length.
# - Suggested filename: strings_intro.py
