# exercise one

i = 0

for i in range(1, 11):
    print(i)

print()

# exercise two

i = 0


while i < 11:
    print(i)
    i += 1

print()

# exercise three

for letter in "joaoluccasmarques29@gmail.com":
    if letter == "@":
        break
    print(letter)

print()

# exercise four

for digit in "0165031806510":
    if digit == "0":
        print("X", end="")
        continue
    print(digit, end="")
