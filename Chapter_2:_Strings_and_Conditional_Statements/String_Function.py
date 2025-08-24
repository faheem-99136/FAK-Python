
"""
STRING METHODS - examples and explanations

This file demonstrates common Python string methods with clear examples
and comments. Variable names avoid shadowing built-ins (don't use `str` as a
variable name in real code).
"""

# Example text we will use for demonstrations
text = "i am a Faheem Alam Khan and I am a boy"
print("Original text:")
print(text)
print()

# 1) endswith / startswith
# - endswith(suffix): returns True if string ends with suffix
# - startswith(prefix): returns True if string starts with prefix
print("Ends with 'boy'?", text.endswith("boy"))
print("Ends with 'han'?", text.endswith("han"))  # 'Khan' ends with 'han'
print("Starts with 'i am'?", text.startswith("i am"))
print()

# 2) capitalize, title, upper, lower
# - capitalize(): makes first character uppercase and rest lowercase
# - title(): capitalizes the first letter of every word
# - upper()/lower(): convert to uppercase/lowercase
print("capitalize():", text.capitalize())
print("title():", text.title())
print("upper():", text.upper())
print("lower():", text.lower())
print()

# 3) replace(old, new)
# - replaces occurrences of old substring with new
print("Replace 'Faheem' with 'Fakhri':", text.replace("Faheem", "Fakhri"))
print("Replace lowercase 'a' with 'A' (every 'a'):", text.replace("a", "A"))
print()

# 4) find, rfind, index
# - find(sub) returns lowest index of sub or -1 if not found
# - rfind(sub) returns highest index of sub or -1 if not found
# - index(sub) is like find but raises ValueError if not found
print("Find 'Faheem' at index:", text.find("Faheem"))
print("Find 'am' at index (first occurrence):", text.find("am"))
print("rfind 'am' (last occurrence):", text.rfind("am"))
try:
	print("index of 'XYZ' (will raise):", text.index("XYZ"))
except ValueError:
	print("index('XYZ') raised ValueError because substring not found")
print()

# 5) count
# - count(sub) returns number of non-overlapping occurrences of sub
print("Count of 'am' in text:", text.count("am"))
print("Count of 'a' in text:", text.count("a"))
print()

# 6) split / join
# - split(): splits on whitespace (or given separator) into a list
# - join(): joins an iterable of strings with the given separator
words = text.split()
print("Split into words:", words)
print("Join words with '-':", "-".join(words))
print()

# 7) strip / lstrip / rstrip
# - strip() removes leading/trailing whitespace
spaced = "   hello world   "
print("strip(): '" + spaced.strip() + "'")
print()

# 8) islower / isupper / isdigit
# - useful checks; note they depend on the whole string
print("Is original text all lower()?", text.islower())
print("Is 'ABC' upper()?", "ABC".isupper())
print("Is '123'.isdigit()?", "123".isdigit())
print()

# 9) useful tip: avoid naming variables 'str' or 'list' - it hides the built-in types

# --- Short summary ---
print("--- Summary ---")
print("Use .replace(), .find(), .count(), .split(), .join(), .strip(), .upper(), .lower(), .title() etc.")



