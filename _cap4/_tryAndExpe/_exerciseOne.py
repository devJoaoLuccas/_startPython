# try fisrt

try:
    age = int(input("Enter your age:\n"))
    print("Your age is", age)
except ValueError:
    print("We don't understand this number")

# try second

try:
    number = int(input("Enter a number:\n"))
    divisor = int(input("Enter a other number:\n"))
    div = number / divisor
    print("The result is:", div)
except ZeroDivisionError:
    print("Division by zero is not allowed in our Universe")
except ValueError:
    print("We don't understand this number")
