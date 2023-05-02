# create a tuple

myTuple = (1, 2, 3, 4)

print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:])
print(myTuple[:-2])

for x in myTuple:
    print(x)

# tuple 2

var = 123
myTuple2 = (1, var)
t1 = (1, )
t2 = (10, 100)

t3 = t1 + t2
t4 = myTuple2 * 2

print("My tuple 2 =", myTuple2)
print("Lens of my tuple =", len(myTuple2))
print("Tuple one =", t1)
print("Tuple two =", t2)
print("Tuple three =", t3)
print("Tuple four =", t4)
