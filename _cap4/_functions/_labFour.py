# BMI Calculate
# BMI = Weight / height

def bmi(wht, hht):
    if hht < 1.05 or hht > 2.15 \
    or wht < 20 or wht > 200:
        return None

    return wht / hht ** 2


print(bmi(80, 1.65))


# sides of triangule calculate

def sideTriangule(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        return False

    return True


print(sideTriangule(1, 1, 1))
print(sideTriangule(1, 2, 4))


# fibonacci calculate

def fiboCalc(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    element1 = element2 = 1
    som = 0

    for i in range(3, n + 1):
        som = element1 + element2
        element1, element2 = element2, som

    return som


for n in range(1, 10):
    print(n, " ---- ", fiboCalc(n))

# fib resume
print()


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


for x in range(1, 10):
    print(x, " ---- ", fib(x))
