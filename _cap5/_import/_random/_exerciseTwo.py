from random import random, seed, choice, sample, randint

seed(0)

for i in range(5):
    print(random())

print()

for i in range(5):
    print(randint(0, 80), end=', ')


myList = (2, 4, 6, 8, 10)

print()

print(choice(myList))
print(sample(myList, 5))
print(sample(myList, 3))
