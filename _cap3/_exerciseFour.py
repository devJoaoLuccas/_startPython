# Swap in python

variableOne = 1
variableTwo = 2
aux = 0

aux = variableOne
variableOne = variableTwo
variableTwo = aux

print("Variable 1 =", variableOne)
print("Variable 2 =", variableTwo, "\n")

# Swap function

variableOne, variableTwo = variableTwo, variableOne

print("Variable 1 =", variableOne)
print("Variable 2 =", variableTwo, "\n")

# exercise Two - Swap Lists

numbers = [10, 5, 8, 25, 14]
aux = len(numbers)

for i in range(aux // 2):
    numbers[i], numbers[aux - i - 1] = numbers[aux - i - 1], numbers[i]

print(numbers)
