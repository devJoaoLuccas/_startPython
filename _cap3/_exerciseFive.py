# variable

myList = [14, 21, 10, 8, 5]
aux = len(myList)
swap = True

while swap:
    swap = False
    for i in range(aux - 1):
        if myList[i] > myList[i + 1]:
            swap = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)
