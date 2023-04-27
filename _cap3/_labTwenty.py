# variable

# step One

beatles = [ ]

print("Step One:", beatles, "\n")

# step Two

beatles.append('Jhon Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')

print("Step Two:", beatles, "\n")

# step Three

for names in range(2):
    name = input("Please enter the name of the Beatle:\n")
    beatles.append(name)

print("Step Three:", beatles, "\n")

# step Four

del beatles[-1]
del beatles[-1]

print("Step Four:", beatles, "\n")

# step Five

name2 = input("Enter the name of the new Beatles:\n")
beatles.insert(0, name2)

print("Step Five:", beatles, "\n")

# testing list legth

print("Testing length:", len(beatles))
