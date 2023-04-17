# variables 

n1 = int(input("Enter the firts number:\n"))
n2 = int(input("Enter the second number:\n"))
n3 = int(input("Enter the third number:\n"))

largerNumber = n1

if largerNumber < n2: largerNumber = n2
if largerNumber < n3: largerNumber = n3

print(largerNumber, "is the larger number")