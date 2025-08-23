# DATA TYPES IN PYTHON
# --------------------
# Python has several built-in data types. Here are the five primary ones:

# (a) Integer: Whole numbers (positive, negative, or zero)
age = 23
temperature = -45
print(type(age))         # Prints: <class 'int'>
print(type(temperature)) # Prints: <class 'int'>

# (b) String: Sequence of characters, always enclosed in quotes
firstname = "Faheem"
secondname = 'Alam'
thirdname = """Khan"""
nickname = '''F.A.K'''
age2025 = "17"           # Even numbers in quotes are strings
wintertemp = '-12'       # Negative numbers in quotes are also strings
print(type(firstname))   # Prints: <class 'str'>
print(type(secondname))  # Prints: <class 'str'>
print(type(thirdname))   # Prints: <class 'str'>
print(type(nickname))    # Prints: <class 'str'>
print(type(age2025))     # Prints: <class 'str'>
print(type(wintertemp))  # Prints: <class 'str'>

# (c) Float: Decimal numbers
price = 45.99
percentage = 97.97
print(type(price))       # Prints: <class 'float'>
print(type(percentage))  # Prints: <class 'float'>

# (d) Boolean: True or False values (must be capitalized)
a = True
b = False
print(type(a))           # Prints: <class 'bool'>
print(type(b))           # Prints: <class 'bool'>

# (e) None: Represents the absence of a value
# Useful for initializing variables that don't have a value yet
d = None
e = None
print(type(d))           # Prints: <class 'NoneType'>
print(type(e))           # Prints: <class 'NoneType'>

# To check the type of any variable, use the built-in type() function.
# This helps you understand what kind of data is stored in a variable.