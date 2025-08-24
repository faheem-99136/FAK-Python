# Lets Practice:->
"""Write a program to ask the user to names of their favorite three persons and store them in a list"""
# So first of all we have to make an empty list to store names
favorite_persons = []

# Now we have to input persons names
prsn1 = input("Enetr 1st person name: ")
prsn2 = input("Enetr 2nd person name: ")
prsn3 = input("Enetr 3rd person name: ")

# Now we have to add this input names to the list
favorite_persons.append(prsn1)
favorite_persons.append(prsn2)
favorite_persons.append(prsn3)

# Names added now we have to print our list
print(favorite_persons)


"""There is another method too for writting the above code"""
favorite_persons = []
prsn = input("Enetr 1st person name: ")
favorite_persons.append(prsn)
prsn = input("Enetr 2nd person name: ")   # Here I don't know why the three variables prsn are the same
favorite_persons.append(prsn)
prsn = input("Enetr 3rd person name: ")
favorite_persons.append(prsn)
print(favorite_persons)


"""There is another method too"""
favorite_persons = []
favorite_persons.append(input("Enetr 1st person name: "))
favorite_persons.append(input("Enetr 2nd person name: "))
favorite_persons.append(input("Enetr 3rd person name: "))
print(favorite_persons)