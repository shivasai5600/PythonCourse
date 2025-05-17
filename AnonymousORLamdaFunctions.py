""" Anonymous Functon OR Lamda Function

==> Anonymous function are those which does not contains any name explicitly.
==> The purpose of Anonymous functions is that 'To perform instant operations'.
==> Instant operations are those which we use at the point of time only and no longer interested to use in
    the further programs/projects.
==> Anonymous functions defenitions contains Single Executable statement.
==> Anonymous functions automically retuns the result after excetuing single statement.
==> To define Anonymous functions, we use lambda keyword and hence anonymous are also called
 lambda functions.
========================= syntax  ==>  varname = lambda params-list : Single Statement
Explanation => 'varname' is an object of <class,'function'>, here varname itself acts name of anonymous function.
==> Lambda is a keyword and used to defined anonymous Functions.
==> param-list represents list of formal parameters and they are used for storing the input values
    coming from function calls
==> Single statement represents valid python executable program """
                      # ========= Example ----------1 =================
# def sum(a,b):      # normal function
#     c=a+b
#     return c
#
# z=lambda a,b:a+b   # anonymous function defenition
#
# #main program
# result=sum(10,20)
# res=z(10,20)
# print("sum of a,b is {}".format(result))
# print(res)

# ============================= Example ----------2 =======================

# rectarea=lambda l,b:l*b                # area of rectagnle
#
# l=float(input("Enter the length:"))
# b=float(input("Enter the breadth:"))
# re1=rectarea(l,b)
# print(f"Area of rectangle is {re1}")
# print("=="*40)
# print("Area of rectangle is {}".format(rectarea(l, b)))

# import matplotlib.pyplot as pt       # random example of pie chart using modulus
# import numpy as np
# ir=["python","java","c","CPP"]
# usage=np.array([60,25,10,5])
# pt.pie(usage,labels=ir)
# pt.show()

# # ============================= Example ----------3 =======================
# findbig=lambda x,y:x if x>y else y
# findsmall=lambda x,y:x if x<y else y
#
# a=int(input("Enter First value:"))
# b=int(input("Enter First value:"))
# print("max({},{})={}".format(a,b,findbig(a,b)))
# print("min({},{})={}".format(a,b,findsmall(a,b)))

# # ============================= Example ----------4 =======================
# findbig=lambda x,y,z:x if (x>y) and (x>z) else y if (y>z) and (y>x) else z
# findsmall=lambda k,v,r:k if (k<v) and (k<r) else v if (v<k) and (v<r) else r
#
# a=int(input("Enter First value:"))
# b=int(input("Enter second value:"))
# c=int(input("Enter third value:"))
# print("max({},{},{})={}".format(a,b,c,findbig(a,b,c)))
# print("min({},{},{})={}".format(a,b,c,findsmall(a,b,c)))

# # ============================= Example ----------5 =======================
# findbig=lambda x,y,z:"Values are equal" if (x==y) and (y==z) and (z==x) else x if (x>y) and (x>z) else y if (y>z) and (y>x) else z
# findsmall=lambda k,v,r:k if (k<v) and (k<r) else v if (v<k) and (v<r) else r
#
# a=int(input("Enter First value:"))
# b=int(input("Enter second value:"))
# c=int(input("Enter third value:"))
# print("max({},{},{})={}".format(a,b,c,findbig(a,b,c)))
# print("min({},{},{})={}".format(a,b,c,findsmall(a,b,c)))

# ============================= Example ----------6 =======================
findbig=lambda ls:max(lst)
findsmall=lambda k:min(lst)

lst=[1,2,3,4,5,6,7,8,9,10]
print("max({})={}".format(lst,findbig(lst)))
print("min({})={}".format(lst,findsmall(lst)))