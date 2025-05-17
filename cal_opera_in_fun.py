# def addop():                                     # first method
#     a=int(input("Enter the 1st number: "))
#     b = int(input("Enter the 2nd number: "))
#     print(f"sum of {a},{b} is {a+b}")
# def subop():
#     a=int(input("Enter the 1st number: "))
#     b = int(input("Enter the 2nd number: "))
#     print(f"sub of {a},{b} is {a-b}")
# def mulop():
#     a=int(input("Enter the 1st number: "))
#     b = int(input("Enter the 2nd number: "))
#     print(f"mul of {a},{b} is {a*b}")
# def divop():
#     a=float(input("Enter the 1st number: "))
#     b = float(input("Enter the 2nd number: "))
#     print(f"div of {a},{b} is {a/b}")
#     print(f"floordiv of {a},{b} is {a // b}")
# def mudop():
#     a=int(input("Enter the 1st number: "))
#     b = int(input("Enter the 2nd number: "))
#     print(f"mudulus of {a},{b} is {a%b}")
# def expop():
#     a=int(input("Enter the 1st number: "))
#     b = int(input("Enter the 2nd number: "))
#     print(f"power of {a},{b} is {a**b}")
#
# #main program
# addop()
# subop()
# mulop()
# divop()
# mudop()
# expop()
print("-"*50)        #secind method
def readvalues(n):
    a = float(input(f"Enter the 1st number {n}"))
    b = float(input(f"Enter the 2nd number {n}"))
    return a,b
def addop():
    a,b = readvalues("addition:")
    print(f"sum of {a},{b} is {a+b}")
def subop():
    a, b = readvalues("subtraction:")
    print(f"sub of {a},{b} is {a-b}")
def mulop():
    a, b = readvalues("multiplication:")
    print(f"mul of {a},{b} is {a*b}")
def divop():
    a, b = readvalues("division")
    print(f"div of {a},{b} is {a/b}")
    print(f"floordiv of {a},{b} is {a // b}")
def mudop():
    a, b = readvalues("modulus:")
    print(f"mudulus of {a},{b} is {a%b}")
def expop():
    a, b = readvalues("exponential:")
    print(f"power of {a},{b} is {a**b}")

addop()
subop()
mulop()
divop()
mudop()
expop()