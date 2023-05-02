# create a dicionary

engToPt = {"cat": "gato", "horse": "cavalo", "cachorro": "dog"}
phoneList = {"João": 71991092619, "Marcos": 71991098671, "Home": 7130350761}
empty = {}

print(engToPt)
print(phoneList)
print(empty)
print()
print(engToPt["cat"])
print(phoneList["João"])
print()

for word in sorted(engToPt.keys()):
    print(word, "---->", engToPt[word])
