stg1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(stg1.index("J"))
print(stg1.index("M"))
print(list(stg1))
print(stg1.count("F"))
print(stg1.count("0"))

stg2 = 'jOãO'
stg3 = 'mArQUEs'

print(stg2.capitalize(), end=' ')
print(stg3.capitalize())

stg4 = 'cicero'

print('[' + stg4.center(30, '*') + ']')
print('[' + stg4.center(30) + ']')

stg5 = 'Messi #10'

print(stg5.isalnum())
print(stg4.isalnum())
print('Messi10'.isalpha())
print('2022'.isdigit())
print('messi'.islower())
print('MESSI'.islower())
print(' '.isspace())
print('MESSI'.isupper())


stg6 = ', '

print(stg6.join(["João Luccas", "Ala", "10"]))
