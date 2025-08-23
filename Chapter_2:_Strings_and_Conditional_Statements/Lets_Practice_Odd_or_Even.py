#Lets Practice:--> 
"""Write a program to check if a number entered by the user is odd or even"""
# For example
num = int(input("Enter the number: "))
remainder = num % 2
if(remainder == 0):  # As we know that even numbers are completely divisible by 2 i.e if a number is divided by 2 it gives remainder = 0 then its an even.
    print("The number you entered is even")
else:
    print("Odd") # if not...