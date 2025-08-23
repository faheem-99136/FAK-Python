
# NEXT LINE & TABS IN STRINGS (beginner friendly)
# You cannot press Enter inside quotes to create a new line; use escape sequences instead.

text_single_line = "I am Faheem. I am reading in GDC Mingora"  # single-line string
print("Single line ->", text_single_line)

# \n inserts a new line inside a string
text_with_newline = "I am Faheem.\nI am reading in GDC Mingora"
print("With \n ->")
print(text_with_newline)

# 	 inserts a tab character
text_with_tab = "I am Faheem.\tI am reading in GDC Mingora"
print("With \t ->")
print(text_with_tab)

# Triple-quoted strings: easier for multi-line text
multi = """I am Faheem.
I am reading in GDC Mingora
This is written on multiple lines using triple quotes."""
print("Triple-quoted multi-line ->")
print(multi)

# Raw strings (prefix r) treat backslashes literally; useful for showing escape sequences or file paths
raw_example = r"Line1\nLine2 (this shows the characters \n, not a newline)"
print("Raw string ->", raw_example)

# When you want to see exactly what characters are in a string (including \n or \t), use repr()
print("repr(text_with_newline):", repr(text_with_newline))

# Practice: try printing strings with different escape sequences and using repr() to inspect them.