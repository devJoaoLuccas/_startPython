# is to write a function checking whether
# a number is prime or not.


def checkPrime(n):

    check = True

    for i in range(2, n):
        if (n % i) == 0:
            check = True
        else:
            check = False

    if check:
        print(n, "isn't a prime number")
    else:
        print(n, "is a prime number")


checkPrime(7)
checkPrime(5)
