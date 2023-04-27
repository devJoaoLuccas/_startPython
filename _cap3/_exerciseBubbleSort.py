# variables

myList = [ ]
num = int(input("Enter how many elements do youn want to sort:"))

for i in range(num):
    elements = input("Enter a list of elements:")
    myList.append(elements)

print("My list before Bublle Sort =", myList)

myList.sort()

print("My list after Bubble Sort =", myList)

# Rever function

myList.reverse()

print("My list after Reverse = ", myList)
