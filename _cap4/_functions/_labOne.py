# Your task is to write and test a function which takes one argument (a year)
# and returns True if the year is a leap year, or False otherwise


def leapYear(year):
    if (year % 4 == 0):
        print(year, "is a leap year!")
    else:
        print(year, "isn't a leap year!")


leapYear(1988)
leapYear(2001)
