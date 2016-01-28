
# read M T X

# M = float(raw_input())
# T = int(raw_input())
# X = int(raw_input())

M = 12.00
T = 20
X = 8

tip = M * T / 100 

tax = M * X / 100

finalPrice = M + tip + tax
finalPrice = int(round(finalPrice))

print("The final price of the meal is $" + str(finalPrice) + ".")