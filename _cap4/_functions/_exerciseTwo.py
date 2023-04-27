
def message(nome):
    print("Hello", nome.upper())


message("joao luccas")


def message2(numero):
    print("This is your number:", numero)


message2("71991092619")


def message3(state, city):
    print("This is your state:", state)
    print("This is your city:", city)


message3("Bahia", "Salvador")
message3("Maranhão", "São Luis")


def message4(fName, lName):
    print("Hello, my name is", fName, lName)


message4("Dick", "Grayson")
message4("Bruce", "Wayne")
message4("Jason", "Tod")


def message5(firstName, lastName):
    print("Hello my name is", firstName, lastName)


message5(firstName="Clark", lastName="Kent")
message5(lastName="Wayne", firstName="Damian")


def sum(a, b, c):
    somar = a + b + c
    print(a, "+", b, "+", c, "=", somar)


sum(14, 20, 22)
sum(21, 10, 8)
