# variables

income = float(input("Enter the anual Personal Income:\n"))

if income <= 85528:
    tax = (income * 0.18) - 556.02
    if tax < 0:
        tax = 0
else:
    tax = (income - 85528) * .32 + 14839

tax = round(tax, 0)

print("The tax is:", tax, "thalers")
