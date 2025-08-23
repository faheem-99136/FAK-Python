# ===============================
# STRING BASICS & OPERATIONS IN PYTHON
# ===============================
# This file covers:
#   - String concatenation
#   - Calculating string length
#   - Type conversion for concatenation
#   - Edge cases and examples
# ===============================

# --- Concatenation ---
# In Python, you can add (concatenate) two or more strings using the + operator.
# This joins the text together, just like adding numbers joins their values.
# Example:
str1 = "Faheem"      # First string
str2 = " Alam"       # Second string (note the space at the start)
str3 = " Khan"       # Third string (note the space at the start)

full_name = str1 + str2 + str3   # Concatenate all three strings into one
print(full_name)                 # Output: 'Faheem Alam Khan'

# You can also concatenate empty strings:
empty = ""
result = str1 + empty
print(result)  # Output: 'Faheem' (no change)

# --- Concatenation with Numbers ---
# You cannot directly add a string and a number:
# print("Age: " + 25)  # This will cause an error!
# You must convert the number to a string first:
age = 25
print("Age: " + str(age))  # Output: 'Age: 25'

# --- Length of String ---
# To calculate the length of a string, use the len() built-in function.
# Spaces, tabs, and special characters are also counted.
str1 = "Faheem"
str2 = "Alam"
str3 = "Khan"
final_str = str1 + str2 + str3  # No spaces between words
print(len(str1))   # Output: 6
print(len(str2))   # Output: 4
print(len(str3))   # Output: 4
print(len(final_str))  # Output: 14

# If you add spaces before 'Alam' and 'Khan', the length increases:
str2 = " Alam"
str3 = " Khan"
final_str = str1 + str2 + str3
print(len(final_str))  # Output: 16 (spaces are counted)

# --- More Examples ---
# Concatenating with special characters:
greeting = "Hello\nWorld"  # \n creates a new line
print(greeting)
print(len(greeting))  # Output: 11 (\n counts as one character)

# Summary:
# - Use + to join strings
# - Use str() to convert numbers before joining
# - Use len() to count all characters, including spaces and special characters
