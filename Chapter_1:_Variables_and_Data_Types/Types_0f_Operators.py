# TYPES OF OPERATORS IN PYTHON
# ---------------------------
# Operators are symbols that perform operations on variables and values.
# Here are the four basic types of operators in Python:

# (a) Arithmetic Operators: +, -, *, /, %, **
a = 20
b = 10
print(a + b)   # Addition: 30
print(a - b)   # Subtraction: 10
print(a * b)   # Multiplication: 200
print(a / b)   # Division: 2.0 (always returns float)
print(a % b)   # Modulo: 0 (remainder)
print(a ** b)  # Exponentiation: 20^10

# (b) Relational/Comparison Operators: ==, !=, >, <, >=, <=
c = 50
d = 20
print(c == d)  # Equal to: False
print(c != d)  # Not equal to: True
print(c > d)   # Greater than: True
print(c < d)   # Less than: False
print(c >= d)  # Greater than or equal to: True
print(c <= d)  # Less than or equal to: False

# (c) Assignment Operators: =, +=, -=, *=, /=, %=, **=
num = 10       # Assigns 10 to num
num += 10      # Adds 10 to num (now 20)
print(num)     # Output: 20

num1 = 90
num1 -= 70     # Subtracts 70 from num1 (now 20)

num2 = 6
num2 *= 3      # Multiplies num2 by 3 (now 18)

num3 = 8
num3 /= 2      # Divides num3 by 2 (now 4.0)

num4 = 16
num4 %= 4      # Modulo operation (now 0)

num5 = 2
num5 **= 3     # Exponentiation assignment (now 8)

# (d) Logical Operators: not, and, or
# These work on Boolean values (True/False)

# NOT operator:
print(not False)         # Returns True
print(not True)          # Returns False

x = 19
y = 18
print(not (x > y))       # Returns False because x > y is True

# AND operator:
val1 = True
val2 = True
print("AND Operator:", val1 and val2)  # Returns True if both are True

# OR operator:
val3 = True
val4 = False
print(val3 or val4)      # Returns True if at least one is True
print((x > y) or (x < y)) # Returns True because x > y is True

# Operators are essential for performing calculations, comparisons, and logic in Python programs!





