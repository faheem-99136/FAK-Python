# ===============================
# PRACTICE: COUNT OCCURRENCE OF CHARACTERS IN STRING
# ===============================
# This file covers:
#   - Counting specific character occurrences in a string
#   - Using str.count() method
#   - More examples and user input
# ===============================

# --- Example 1: Count '$' in a string ---
text = "Hi! $, I am $ symbol like $99.99"
count_dollar = text.count("$")
print(f"Number of '$' in the string: {count_dollar}")

# --- Example 2: Count other characters ---
count_exclamation = text.count("!")
print(f"Number of '!' in the string: {count_exclamation}")

# --- Example 3: User input ---
user_text = input("Enter any string: ")
char_to_count = input("Enter character to count: ")
print(f"Number of '{char_to_count}' in your string: {user_text.count(char_to_count)}")

# --- Notes ---
# - str.count(substring) returns the number of times substring appears in the string.
# - You can count any character or substring, not just single characters.
