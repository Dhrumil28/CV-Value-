import math

#Getting values from the users

X = float(input("Enter the Flow Rate :"))
Y = float(input("Enter the Pressure Drop :"))
Z = float(input("Enter specific Gravity of Material :"))

A = Z/Y
EQ = X*pow(A,1/2)

print(EQ )
