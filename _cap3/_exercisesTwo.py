# exercise one - Lists

numbers = [10, 5, 7, 2, 1]
print("Original list of numbers", numbers)  # Printing original list content.

numbers[1] = 14  # Add new number for 1
print("Modified list of nunmbers", numbers)  # Printing original list content.

numbers[4] = numbers[1]  # Copying value of the second element to fifht
print("Second modified list of numbers", len(numbers))

# exercise two - Lists

numeros = [21, 14, 10, 8, 17]
print("Numeros =", numeros)
print("Len of Numeros =", len(numeros))

del numeros[4]
print("Numeros after del =", numeros)
print("Len of Numeros =", len(numeros), "\n")

# exercise three - Lists

print("Firts numero =", numeros[-4])
print("Second numero =", numeros[-3])

# exercise four - Lists

testing = [14, 21, 22, 17]

print("len 1 =", len(testing))
print("List 1 =", testing, "\n")

testing.append(3)

print("Len 2 =", len(testing))
print("List 2 =", numbers, "\n")

testing.insert(0, 10)

print("Len 3 =", len(numbers))
print("List 3 =", numbers)
