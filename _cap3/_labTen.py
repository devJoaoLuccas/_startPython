# variables

year = int(input("Enter a year:\n"))

if year % 4 != 0:
    print("It's a comomm year")
elif year % 100 != 0:
    print("It's a leap year")
elif year % 400 != 0:
    print("It's a commom year")
else:
    print("It's a leap year")
