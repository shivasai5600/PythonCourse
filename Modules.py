# In this 'Modules' file acts as a Module in the other file to access of its programs.
#----------------------------------------------------------------------------------------------------
""""
==> We know that Functions concept makesus understand how to perform the operations and How to
        Re-Use the function code within the same program.But Functions concept unable to provided
        reusability accross the programs
==> To Re-Use the code across the program, In pyhton we havwe a concept called MODULES
==> THe purpose of Modules is that 'TO RE-USE code accross the programs'
------------------------------------------------------------------------------------------------------
Definition of a module : A MODULE is a Collection of Variables, Functions and Classes.
------------------------------------------------------------------------------------------------------
-----------------------------------------Types of Modules --------------------------------------------
In Python we have Two Types of Modules.
a) Pre-Defined or Built-In-Modules
b) Programmer or User or Custom-defined Modules
-------------------------------------------------------------------------------------------------------------------
a) Pre-Defined or Built-In-Modules -------------
==> These Modules are developed by language developers and THey are available in Python API and whose role is to deal
    with the Universal Requirements.
    EXAMPLES -------- : functools,sys,os,re,threading,cx_Oracle,my-sqlconnector,time......etc
-------------------------------------------------------------------------------------------------------------------
b) Programmer or User or Custom-defined Modules---------------
==> These Modules are developed by language programmers and THey are available in Python Project and whose role is to deal
    with the Common Requirements.
    EXAMPLES -------- : user defined modules.."""
def addop(a,b):
    print(a+b)

# #============== EXAMPLE --2 =================================
# def readnes():
#     print("ENter the values seperated by space:")
#     lst=[str(names) for names in input().split()]
#     return lst
# def dispnames(names):
#     print("="*50)
#     for name in names:
#         print("{}".format(name))
#     else:
#         print("="*50)
# def sortnames():
#     names=readnes()
#     print("="*50)
#     print("Original names:")
#     dispnames(names)
#     # sort the names in Ascending order
#     names.sort()
#     print("Sorted Names in the Ascending order")
#     dispnames(names)
#     # sort the names in Decending order
#     print("Sorted Names in the Decending order")
#     names.sort(reverse=True)
#     dispnames(names)

#============== EXAMPLE --3 =================================
def menu():
    print("="*50)
    print("A r i t h m e t i c === O p e r a t i o n s")
    print("="*50)
    print("\t1.Addtion Operaation")
    print("\t2.Subtraction Operaation")
    print("\t3.Multiplicaion Operaation")
    print("\t4.Division Operaation")
    print("\t5.Modulus Operaation")
    print("\t6.Exponential Operaation")
    print("\t7.Exit")
    print("=" * 50)
