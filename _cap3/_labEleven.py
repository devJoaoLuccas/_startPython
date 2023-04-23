# variables

largestNumber = -9999999

number = int(input("Enter a number or type -1 to stop:\n"))

while number != -1:
    if number > largestNumber:
        largestNumber = number

    number = int(input("Enter a number or type -1 to stop:\n"))

print("The largest number is:", largestNumber)
