stg1 = 'Marques Marolento'

for i in range(len(stg1)):
    print(stg1[i], end=' ')

print("\n")

print(stg1[8:])

print()

stg2 = 'Vou machucar no talento'

for character in range(len(stg2)):
    print(stg2[character], end=' ')

print("\n")


print("Marolento" in stg1)
print("Marolento" not in stg2)
print("no talento" in stg2)
print("Machucar" in stg1)
print("Marques" not in stg1)

del stg1
print()

print("Pede pra ser violento " + stg2)

print(min(stg2))
print(max(stg2))
