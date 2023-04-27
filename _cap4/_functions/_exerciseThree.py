

def happyNewYear(whises=True):
    print("Three...")
    print("Two...")
    print("One...")

    if not whises:
        return

    print("Happy New Year")


happyNewYear()
print("")
happyNewYear(False)
print("")


def boring_function():
    print("'Boredom Mode' ON.")
    return 123


print("This leason is interesting!")
boring_function()
print("This leason is boring")
print("")


def noneTest(x):
    if x is None:
        print("I'm Sorry you don't carry any value")
    else:
        print("Your value is:", x)


noneTest(x=None)
noneTest(x=9)
print("")


def testPair(a, b):
    sum = a + b

    if (sum % 2 == 0):
        return True
    else:
        return False


print(testPair(2, 2))
print(testPair(1, 2))
print("")


def strangeList(n):
    list = []

    for i in range(1, n + 1):
        list.append(i)

    return list


print(strangeList(10))
