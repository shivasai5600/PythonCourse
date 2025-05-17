""" ==============================  APPROACH === ONE  =============================="""
# a=int(input("enter number a:"))
# b=int(input("enter number b:"))
# w=int(input("enter number w:"))
# s=int(input("enter number s:"))
# def sumop(x, y):
#     z=x+y
#     return z
# result = sumop(a, b)
# result1 = sumop(w, s)
# print("The sum is:", result)
# print("The sum is:", result1)
""" ==============================  APPROACH === TWO  =============================="""
# def sumop():
#     a = int(input("enter number a:"))
#     b = int(input("enter number b:"))
#     return a+b
# d = sumop()
# print(d)
"""========write a python program which will calculate square root of a given number by using functions====="""
# a=int(input("Enter the square root of a number: "))
# c=a**0.5
# print(f"{c}")

# def squareroot(n):         #approach 1 calling inside of function call
#     result = n**0.5
#     return result
#
# x=int(input("Enter the number:"))
# res = squareroot(x)
# print(f"square root of nymber is: {res}")

# def squareroot():         #approach 2   calling inside the function body, result also in dunction body
#     n = int(input("Enter the number:"))
#     result = n**0.5
#     print(f"square root of nymber is: {result}")
# squareroot()

# def squareroot(n):         #approach 3   calling inside the function call, result in function body
#     result = n**0.5
#     print(f"square root of nymber is: {result}")
# n=float(input("Enter the number:"))
# squareroot(n)


# def squareroot():
#     n=float(input("Enter the number:"))       #approach 4   calling inside the function body, result in function call
#     result = n**0.5
#     return n,result
#
# x,y = squareroot()
# print(f"squareroot of {x} is {y}")
# print("====or=========")
# result = squareroot()
# print("squareroot({}) = {}".format(result[0],result[1])

# write a python program which will calculate area  of rectangle by using functions(use all approaches)
# write a python program which will swap any type of values
# write a pytho program which will calculate area and perimeter of a square
# write a python program which will calculate area and perimeter of rectangle

# write a python program which will accept list of names and sort them in both desc and ascending order using functions
def readnames():
    n=int(input("Enter the number of names: "))
    if n<=0:
        return None
    else:
        lst=list()
        for i in range(1,n+1):
            name = input("Enter {} name: ".format(i))
            lst.append(name)
        return lst

def displaynames(names):
    print("-"*50)
    for name in names:
        print("\t{}".format(name))
    print("-"*50)

def sortnames(stnames):
    # sort the names in ascending order
    stnames.sort()
    print("Names in Ascending order")
    displaynames(stnames)
    stnames.sort(reverse=True)
    print("Names in Decending order")
    displaynames(stnames)

names = readnames()
if(names==None):
    print("invalid")
else:
    print("-"*50)
    print("Original names")
    displaynames(names)
    sortnames(names)

