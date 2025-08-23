# INPUT IN PYTHON
# --------------
# The input() function is used to accept values from the user via the keyboard.
# By default, input() returns a string.

# Example: Accepting a name from the user
name = input("Enter your name: ")
print("Welcome", name)  # Greets the user with their name

# To accept numbers, you need to convert the input to the desired type:
# Accepting an integer from the user
age = int(input("Enter your age: "))
print("Nice", age, "years")  # Prints the age entered by the user

# Accepting a floating-point number from the user
price = float(input("Enter your price: "))  # Converts input to float

# Summary:
# input()         -> always returns a string
# int(input())    -> converts input to integer
# float(input())  -> converts input to float

# You can use these conversions to get the correct data type for your program!


