import math

b1 = int(input("Enter the Inlet pressure :- "))
b2 = int(input("Enter the Outlet pressure :- "))
x = b1 - b2
Area = int(input("Enter the Area of Pipe :- "))
A1 = int(input("Area of inlet :- "))
A2 = int(input("Area of Outlet :- "))
Z = A1/A2

def volumetric_flow(density):
    A = pow(x,1/2)*Area*pow(2,1/2)
    B = pow((density*(1-pow(Z,2))),1/2)
    y = A/B
    return y


final = volumetric_flow(0.354)
print (final)
